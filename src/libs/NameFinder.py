import requests

from libs.TvDbConnector import _TvDbConnector
from libs.TvDbResponseParser import TvDbResponseParser
from libs.TvFile import TvFile


class NameFinder:

    def __init__(self, tv_db: _TvDbConnector, response_parser: TvDbResponseParser):
        self._tv_db = tv_db
        self._response_parser = response_parser


    def get_episode_name(self, tv_file: TvFile):
        search_name = tv_file.clean_src_name

        if not search_name:
            return None

        try:
            show_id = self._response_parser.get_show_id(
                response=self._tv_db.search_for_series(search_name),
                search=search_name,
                year_premiered=tv_file.year
            )

            return self._response_parser.get_episode_name(
                episodes=self._tv_db.get_episode_info(show_id),
                season_num=tv_file.season_num,
                episode_num=tv_file.episode_num
            )

        except requests.ConnectionError:
            return None
