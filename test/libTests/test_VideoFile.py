from math import inf

import pytest

from lib.VideoFile import VideoFile


class TestVideoFile:

    @pytest.mark.regression
    @pytest.mark.parametrize("ans", [
        "cool", "very_long_answerThatISCASE_SENSITVE", "o"
    ])
    def test_get_extension_in_file_name(self, ans, monkeypatch):
        monkeypatch.setattr(VideoFile, "_get_file_info", lambda x: None)

        video = VideoFile("", "foo.4rj3iofjro.{}".format(ans))
        video._get_extension()

        assert video._ext == video.extension == ans

    @pytest.mark.regression
    @pytest.mark.parametrize("in_put", [
        "2100", "2099", "2000", "1999", "1100", "1099"
    ])
    def test_get_year_in_file_name(self, in_put, monkeypatch):
        monkeypatch.setattr(VideoFile, "_get_file_info", lambda x: None)

        video = VideoFile("", "foo.{}.4rj3iofjro.sdf".format(in_put))
        video._get_year()

        if 1100 <= int(in_put) <= 2099:
            assert video._year == video.year == in_put
        else:
            assert video._year is video.year is None


    @pytest.mark.regression
    @pytest.mark.parametrize("in_put, ans", [
        ("1080", "1080p"), ("1080p", "1080p"), ("1080P", "1080p"),
        ("720", "720p"), ("720p", "720p"), ("720P", "720p"),
        ("7211P", None), ("1081p", None)
    ])
    def test_get_resolution_in_file_name(self, in_put, ans, monkeypatch):
        monkeypatch.setattr(VideoFile, "_get_file_info", lambda x: None)

        video = VideoFile("", "foo.{}.4rj3iofjro.sdf".format(in_put))
        video._get_resolution()

        assert video._res == (in_put if ans else None)
        assert video.res == ans

    @pytest.mark.regression
    @pytest.mark.parametrize("src_name", ["popGoesTheWeasel"])
    @pytest.mark.parametrize("year, res, ans", [
        ("GOES", "The", 3),
        ("The", "est", 5),
        (None, "oest", 4),
        ("ease", None, 11),
        (None, None, inf),
        ("foo", "boo", inf)
    ])
    def test_get_trim_index_to_cleanup_name(self, src_name, year, res, ans, monkeypatch):
        monkeypatch.setattr(VideoFile, "_get_file_info", lambda x: None)
        video = VideoFile("", src_name)
        video._year = year
        video._res = res

        assert video._get_src_name_trim_index() == ans

    @pytest.mark.regression
    def test_get_cleaned_src_name(self, monkeypatch):
        seeder = "[loop54Baz]"
        monkeypatch.setattr(VideoFile, "_get_file_info", lambda x: None)
        monkeypatch.setattr(VideoFile, "_get_src_name_trim_index", lambda x: 30)
        monkeypatch.setattr(VideoFile, "_search", lambda x, y, z: seeder)

        video = VideoFile("", "{} (Video.Show.foo}}](.garbageToBeRemoved".format(seeder))
        video._get_cleaned_src_name()

        assert video._clean_src_name == "Video Show Foo"

    @pytest.mark.regression
    @pytest.mark.parametrize("in_put, ans", [
        ("The.legend.of.Carl.2018.LOOK_AT_ME.720p.Red.Cool.Varg.Loo.avi", "The Legend Of Carl [2018][720p].avi"),
        ("this.title has.nothing in It.mp4", "This Title Has Nothing In It.mp4"),
        ("[foobBar.Legend]Copper.Legend, Rock{(1080P).Borot.2054}.mkv", "Copper Legend, Rock [2054][1080p].mkv")
    ])
    def test_get_base_name(self, in_put, ans):
        assert VideoFile("", in_put).base_name == ans

    @pytest.mark.regression
    @pytest.mark.parametrize("year", ["2180", None])
    def test_get_destination_path(self, year, monkeypatch):
        clean = "foo"

        monkeypatch.setattr(VideoFile, "_get_file_info", lambda x: None)

        video = VideoFile("", "")
        video._clean_src_name = clean
        video._year = year

        if year:
            assert video.dest_path == clean + " [{}]".format(year)
        else:
            assert video.dest_path == clean
