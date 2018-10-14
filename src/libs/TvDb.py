import json
import requests


class TvDb:

    class _Decorators:

        @classmethod
        def check_valid_response(cls, bad_response_codes: tuple):
            def _check_valid_response(func):
                def wrapper(*args, **kwargs) -> json:

                    response = func(*args, **kwargs)
                    
                    if response.status_code in bad_response_codes:
                        raise requests.ConnectionError(
                            "'{}' Failed to retrieve info from TvDb, Response Code: '{}'\n\tError: '{}'"
                            .format(func.__name__, response.status_code, response.json().get("Error", None))
                        )

                    return response.json()
                return wrapper
            return _check_valid_response

        @classmethod
        def dedupe(cls, existing_values: dict):
            def _dedupe(func):
                def wrapper(*args, **kwargs):
                    val = existing_values.get(args[1], None)

                    if val:
                        return val

                    val = func(*args, **kwargs)
                    existing_values[args[1]] = val

                    return val
                return wrapper
            return _dedupe

    _AUTHORIZATION = "Authorization"

    _URL_BASE = "https://api.thetvdb.com/"
    _HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        _AUTHORIZATION: None
    }
    _SERIES = dict()
    _EPISODE_INFO = dict()

    def __init__(self, api_key, user_key, user_name):
        self._login_params = json.dumps(
            dict(apikey=api_key, userkey=user_key, username=user_name)
        )

    def retrieve_access_token(self) -> "TvDb":
        self._HEADERS[self._AUTHORIZATION] = "Bearer {}".format(self._retrieve_token().get("token", None))
        return self

    @_Decorators.check_valid_response((401,))
    def _retrieve_token(self) -> requests.post:
        # todo - Implement a thread to refresh JWT as needed
        return requests.post(self._URL_BASE + "login", headers=self._HEADERS, data=self._login_params)

    @_Decorators.dedupe(_SERIES)
    def search_for_series(self, series_name: str) -> requests.get:
        return self._get(self._URL_BASE + "search/series", params=dict(name=series_name))

    @_Decorators.dedupe(_EPISODE_INFO)
    def get_episode_info(self, show_id: int) -> requests.get:
        return self._get(self._URL_BASE + "episodes/{}".format(show_id))

    @_Decorators.check_valid_response((401, 404))
    def _get(self, url: str, params: dict= None) -> requests.get:
        return requests.get(url, headers=self._HEADERS, params=params)
