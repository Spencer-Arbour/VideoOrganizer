import pytest

from libs.TvDbResponseParser import TvDbResponseParser


class TestTvDbResponseParserGetEpisodeName:
    _SEASON = "airedSeason"
    _EPISODE = "airedEpisodeNumber"
    _NAME = "episodeName"
    _DATA = "data"

    @pytest.mark.regresion
    def test_get_episode_name_returns_none_if_empty_data(self):
        episodes = {self._DATA: []}
        name = TvDbResponseParser.get_episode_name(episodes, 0, 0)
        assert name is None

    @pytest.mark.regresion
    def test_get_episode_name_returns_none_if_no_data(self):
        episodes = {}
        name = TvDbResponseParser.get_episode_name(episodes, 0, 0)
        assert name is None

    @pytest.mark.regression
    def test_get_episode_name_returns_correct_name(self, monkeypatch):
        class Faker:
            _true_index = 0

            # noinspection PyUnusedLocal
            @staticmethod
            def fake(*args):
                Faker._true_index += 1
                return Faker._true_index == 3

        monkeypatch.setattr(TvDbResponseParser, "_is_correct_episode", Faker.fake)
        episodes = {self._DATA: [
            {self._NAME: "foo"},
            {self._NAME: "bar"},
            {self._NAME: "bin"},
            {self._NAME: "ban"}
        ]}
        name = TvDbResponseParser.get_episode_name(episodes, 0, 0)
        assert name == "bin"

    @pytest.mark.regresion
    @pytest.mark.parametrize("in_put, ans", [
        ([{_SEASON: 2, _EPISODE: 4}, 2, 4], True),
        ([{_SEASON: 2, _EPISODE: 2}, 2, 4], False),
        ([{_SEASON: 1, _EPISODE: 4}, 2, 4], False),
        ([{_SEASON: 1}, 1, 4], False),
        ([{_EPISODE: 4}, 1, 4], False),
        ([{_SEASON: 1}, 6, 6], False),
        ([{_EPISODE: 4}, 6, 6], False),
        ([{}, 6, 6], False)
    ])
    def test_is_correct_episode(self, in_put, ans):
        is_episode = TvDbResponseParser._is_correct_episode(*in_put)
        assert is_episode is ans
