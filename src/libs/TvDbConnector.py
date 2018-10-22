import json
import requests


class TvDbConnectorSingleton:

    _TV_DB_CONNECTOR = None

    def __new__(cls, *args, **kwargs):

        if not cls._TV_DB_CONNECTOR:
            cls._TV_DB_CONNECTOR = _TvDbConnector(*args, **kwargs).retrieve_access_token()

        return cls._TV_DB_CONNECTOR


class _TvDbConnector:

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

    def retrieve_access_token(self) -> "_TvDbConnector":
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
    def get_episode_info(self, show_id: int, page: int=1) -> requests.get:
        response = self._get(self._URL_BASE + "series/{}/episodes?page={}".format(show_id, page))

        # todo - need to write unit tests for getting new pages
        links = response.get("links", None)
        if links:
            next_page = links.get("next", None)

            if next_page:
                page = self.get_episode_info(show_id, page=next_page)
                response.get("data").extend(page.get("data", None))

        return response

    @_Decorators.check_valid_response((401, 404))
    def _get(self, url: str, params: dict= None) -> requests.get:
        return requests.get(url, headers=self._HEADERS, params=params)
