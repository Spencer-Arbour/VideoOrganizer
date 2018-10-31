import requests

from gui.FileView import FileView
from gui.TvDbConnProblem import TvDbConnProblem
from gui.menu_bar.Config import Config
from gui.templates.StandardButton import StandardButton
from libs.NameFinder import NameFinder
from libs.TvDbConnector import TvDbConnectorSingleton
from libs.TvDbResponseParser import TvDbResponseParser
from libs.TvFile import TvFile
from libs.VideoFileFactory import video_file_factory


class FileToProcessSelector:

    def __init__(self, main_frame):
        self._main_frame = main_frame

        self._search_button = StandardButton(self._main_frame, text="Process Files", command=self._process_files) \
            .grid(row=5, column=1)

    def _process_files(self):
        try:
            tv_db = TvDbConnectorSingleton(
                api_key=Config.API_KEY,
                user_key=Config.UNIQUE_ID,
                user_name=Config.USERNAME
            )
        except requests.ConnectionError:
            if not TvDbConnProblem().process:
                return
            else:
                name_finder = False

        else:
            name_finder = NameFinder(
                tv_db=tv_db,
                response_parser=TvDbResponseParser()
            )

        for directory, file in FileView.get_fileview(self._main_frame).get_files():
            video = video_file_factory(directory, file)
            if name_finder or type(video) == TvFile:
                video.episode_name = name_finder.get_episode_name(video)
            print(video.base_name)
