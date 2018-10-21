import pytest

from libs.FilmFile import FilmFile
from libs.TvFile import TvFile
from libs.VideoFileFactory import video_file_factory


class TestVideoFIleFactory:
    
    @pytest.mark.regression
    @pytest.mark.parametrize("name, expected", [
        ("s9e1", TvFile),
        ("S7E2", TvFile),
        ("s10e94", TvFile),
        ("S57E43", TvFile),
        ("S546E904", FilmFile),
        ("E45S76", FilmFile)
    ])
    def test_get_(self, name, expected):
        assert type(video_file_factory("", name)) == expected
