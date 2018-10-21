from gui.FileView import FileView
from gui.templates.StandardButton import StandardButton
from libs.VideoFileFactory import video_file_factory


class FileToProcessSelector:

    def __init__(self, main_frame):
        self._main_frame = main_frame

        self._search_button = StandardButton(self._main_frame, text="Process Files", command=self._process_files) \
            .grid(row=5, column=1)

    def _process_files(self):
        for directory, file in FileView.get_fileview(self._main_frame).get_files():
            video = video_file_factory(directory, file)
            print(video.base_name)
