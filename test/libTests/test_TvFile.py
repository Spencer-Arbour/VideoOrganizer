from math import inf

import pytest

from lib.TvFile import TvFile


class TestTvFile:

    @pytest.mark.regression
    @pytest.mark.parametrize("in_put, season, episode", [
        ("S05E90", "05", "90"),
        ("s9e4", "9", "4"),
        ("S100e90", None, None),
        ("e90s8", None, None)
    ])
    def test_get_resolution_in_file_name(self, in_put, season, episode, monkeypatch):
        monkeypatch.setattr(TvFile, "_get_file_info", lambda x: None)

        video = TvFile("", "foo.{}.4rj3iofjro.sdf".format(in_put))
        video._get_season_and_episode()

        if season:
            assert video._season == season
            assert video.season == int(season)
        else:
            assert video._season is None
            assert video.season is None

        if episode:
            assert video._episode == episode
            assert video.episode == int(episode)
        else:
            assert video._episode is None
            assert video.episode is None

    @pytest.mark.regression
    @pytest.mark.parametrize("s_char, e_char", [("S", "E"), ("s", "e"), ("S", "e"), ("s", "e"), ("E", "S")])
    @pytest.mark.parametrize("src_name, index", [
        ("foo{se}.{res}.{year}", 3),
        ("foo{se}.{year}.{res}", 3),
        ("foo{res}.{se}.{year}", 3),
        ("foo{res}.{year}.{se}", 3),
        ("foo{year}.{se}.{res}", 3),
        ("foo{year}.{res}.{se}", 3),

    ])
    def test_get_trim_index_to_cleanup_name(self, s_char, e_char, src_name, index, monkeypatch):
        res = "1080p"
        year = "2010"

        season = "5"
        episode = "6"
        se = s_char + season + e_char + episode

        monkeypatch.setattr(TvFile, "_get_file_info", lambda x: None)
        video = TvFile("", src_name.format(se=se, year=year, res=res))
        video._year = year
        video._res = res
        video._season = season
        video._episode = episode

        print(video._get_src_name_trim_index())