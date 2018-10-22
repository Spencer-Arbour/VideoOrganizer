import pytest
from gui.ShowChooser import ShowChooser
from libs.TvDbResponseParser import TvDbResponseParser



class TestTvDbResponseParserGetId:
    _ID = "id"
    _OVERVIEW = "overview"
    _FIRST_AIRED = "firstAired"
    _DATA = [
        {_ID: 1, _OVERVIEW: "foo", _FIRST_AIRED: "2013"},
        {_ID: 2, _OVERVIEW: "bar", _FIRST_AIRED: "2001"},
        {_ID: 3, _OVERVIEW: "", _FIRST_AIRED: "2019-01-23"},
        {_ID: 4, _OVERVIEW: "ban", _FIRST_AIRED: "2013-01-23"},
        {_ID: 5, _OVERVIEW: "pin", _FIRST_AIRED: "2016"},
        {_ID: 6, _OVERVIEW: "", _FIRST_AIRED: ""}
    ]

    @pytest.mark.regression
    def test_get_show_id_returns_none_if_data_empty(self):
        response = {"data": []}
        show_id = TvDbResponseParser.get_show_id("", response)
        assert show_id is None

    @pytest.mark.regression
    def test_get_show_id_returns_none_if_no_data(self):
        response = {}
        show_id = TvDbResponseParser.get_show_id("", response)
        assert show_id is None

    @pytest.mark.regression
    def test_get_show_id_returns_whatever_get_id_returns(self, monkeypatch):
        test_id = 645
        monkeypatch.setattr(TvDbResponseParser, "_get_possible_shows", lambda x, y: [])
        monkeypatch.setattr(TvDbResponseParser, "_get_id", lambda x, y: test_id)

        response = {"data": ["foo"]}
        show_id = TvDbResponseParser.get_show_id("", response)
        assert show_id == test_id

    @pytest.mark.regression
    @pytest.mark.parametrize("year, that_year_usage", [("FakeYear", 1), (None, 0)])
    def test_get_possible_shows_uses_proper_method(self, year, that_year_usage, monkeypatch):
        class Faker:
            def __init__(self, show_id):
                self.usages = 0
                self._show_id = show_id

            # noinspection PyUnusedLocal
            def fake(self, *args):
                self.usages += 1
                return self._show_id

        fake_premiering_that_year = Faker("foo")
        monkeypatch.setattr(TvDbResponseParser, "_get_shows_premiering_that_year", fake_premiering_that_year.fake)

        shows = TvDbResponseParser._get_possible_shows(["bar"], year)

        assert fake_premiering_that_year.usages == that_year_usage
        assert shows == "foo" if fake_premiering_that_year == 1 else "bar"

    @pytest.mark.regression
    def test_shows_premiering_that_year_returns_shows_of_that_year_and_without_first_air_date(self):
        ans = TvDbResponseParser._get_shows_premiering_that_year(self._DATA, "2013")
        assert len(ans) == 3

    @pytest.mark.regression
    def test_return_none_if_data_empty(self):
        show_id = TvDbResponseParser._get_id("", [])
        assert show_id is None

    @pytest.mark.regression
    def test_return_show_id_if_only_one_option(self):
        test_id = 34
        show_id = TvDbResponseParser._get_id("", [{self._ID: test_id}])
        assert show_id == test_id

    @pytest.mark.regression
    @pytest.mark.parametrize("show, ans", [({"id": 99}, 99), (None, None)])
    def test_return_show_chooser_id_if_multiple_choices(self, show, ans, monkeypatch):
        class Fake:
            @property
            def fake(self):
                return show

        monkeypatch.setattr(ShowChooser, "show", Fake().fake)
        monkeypatch.setattr(ShowChooser, "_header", lambda *args: None)
        monkeypatch.setattr(ShowChooser, "_body", lambda *args: None)
        monkeypatch.setattr(ShowChooser, "_footer", lambda *args: None)
        monkeypatch.setattr(ShowChooser, "wait_window", lambda *args: None)

        show_id = TvDbResponseParser._get_id("", [{self._ID: 12}, {self._ID: 22}], False)
        assert show_id == ans

    @pytest.mark.regression
    def test_only_return_shows_with_overview(self):
        shows = TvDbResponseParser._eliminate_shows_without_overview(self._DATA)
        assert len(shows) == 4
