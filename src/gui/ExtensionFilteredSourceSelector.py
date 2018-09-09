from tkinter import Frame, Button


from gui.ExtensionFilter import ExtensionFilter
from gui.FileView import FileView
from gui.SourceDirectory import SourceDirectory
from gui.WarningPopUps import need_valid_directory
from gui.templates.StandardButton import StandardButton
from lib.DirectoryChecks import is_directory_exist
from lib.FileGetter import get_files
from lib.FoundFIles import FoundFiles
from lib.ParseExtensions import parse_extensions


class ExtensionFilteredSourceSelector:

    def __init__(self, main_frame: Frame):
        self._main_frame = main_frame

        self._search_button = StandardButton(self._main_frame, text="Search", command=self._find_files)\
            .grid(row=1, column=1)


    def _find_files(self):

        src_dir = SourceDirectory.get_entry(self._main_frame).get()

        if not is_directory_exist(src_dir):
            need_valid_directory(src_dir)
            return

        ext_filter = parse_extensions(
            ExtensionFilter.get_entry(self._main_frame).get()
        )

        files = FoundFiles.store_files_before_returning(
            get_files(src_dir, ext_filter)
        )

        FileView.get_fileview(self._main_frame).add_files(files)
