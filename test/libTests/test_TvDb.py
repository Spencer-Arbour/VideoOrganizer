from itertools import count

import pytest
import requests

from lib.TvDb import TvDb


class TestTvDb:

    @pytest.mark.regression
    def test_proper_token_retrieved(self, monkeypatch):
        fake = TvDbFake({"token": "foo"})
        monkeypatch.setattr(requests, "post", lambda url, headers, data: fake)

        tv_db = TvDb("fake", "lie", "nope").retrieve_access_token()
        assert tv_db._HEADERS.get("Authorization") == "Bearer foo"

    @pytest.mark.regression
    def test_authorization_error_when_retrieving_token(self, monkeypatch):
        fake = TvDbFake({"Error": "Fake Error"}, 401)
        monkeypatch.setattr(requests, "post", lambda url, headers, data: fake)

        with pytest.raises(requests.ConnectionError) as excinfo:
            TvDb("fake", "lie", "nope").retrieve_access_token()

        assert "Fake Error" in str(excinfo.value)

    @pytest.mark.regression
    def test_get_returns_json(self, monkeypatch):
        fake = TvDbFake({"show_info": "foo"})
        monkeypatch.setattr(requests, "get", lambda url, headers, params: fake)

        tv_db = TvDb("fake", "lie", "nope")._get("fake_url")
        assert tv_db == {"show_info": "foo"}

    @pytest.mark.regression
    @pytest.mark.parametrize("error_code", [401, 404])
    def test_authorization_error_when_retrieving_token(self, error_code, monkeypatch):
        fake = TvDbFake({"Error": "Fake Error"}, error_code)
        monkeypatch.setattr(requests, "get", lambda url, headers, params: fake)

        with pytest.raises(requests.ConnectionError) as excinfo:
            TvDb("fake", "lie", "nope")._get("fake")

        assert "Fake Error" in str(excinfo.value)

    @pytest.mark.regrssion
    def test_search_for_series_only_does_same_search_once(self, monkeypatch):
        call_counts = count()
        monkeypatch.setattr(TvDb, "_get", lambda x, url, params: str(next(call_counts)))

        tv_db = TvDb("fake", "lie", "nope")
        first_fake = tv_db.search_for_series("Fake")
        first_flam = tv_db.search_for_series("Flam")
        second_fake = tv_db.search_for_series("Fake")

        assert first_fake == second_fake == "0"
        assert first_flam == "1"

    @pytest.mark.regrssion
    def test_search_for_episodes_only_does_same_search_once(self, monkeypatch):
        call_counts = count()
        monkeypatch.setattr(TvDb, "_get", lambda x, url: str(next(call_counts)))

        tv_db = TvDb("fake", "lie", "nope")
        first_fake = tv_db.get_episode_info(45)
        first_flam = tv_db.get_episode_info(76)
        second_fake = tv_db.get_episode_info(45)

        assert first_fake == second_fake == "0"
        assert first_flam == "1"

class TvDbFake:
    def __init__(self, json: dict, status_code: int = 200):
        self._json = json
        self._status_code = status_code

    @property
    def status_code(self) -> int:
        return self._status_code

    def json(self) -> dict:
        return self._json
