import pytest

from lib.FilmFile import FilmFile
from lib.TvFile import TvFile
from lib.VideoFileFactory import video_file_factory


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
