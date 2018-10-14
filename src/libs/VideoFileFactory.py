from libs.FilmFile import FilmFile
from libs.TvFile import TvFile
from libs.VideoFile import VideoFile


def video_file_factory(src, name):
    return (TvFile if VideoFile._TYPE_RE.search(name) else FilmFile)(src, name)
