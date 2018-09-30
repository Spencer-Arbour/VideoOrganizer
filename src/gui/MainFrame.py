from tkinter import Frame, E, W, N, S, SUNKEN

from gui.DestinationDirectory import DestinationDirectory
from gui.DestinationSelector import DestinationSelector
from gui.ExtensionFilter import ExtensionFilter
from gui.ExtensionFilteredSourceSelector import ExtensionFilteredSourceSelector
from gui.FileToProcessSelector import FileToProcessSelector
from gui.FileView import FileView
from gui.SourceDirectory import SourceDirectory
from gui.SourceSelector import SourceSelector


class MainFrame:

    _MAIN = "main"

    def __init__(self, root):
        self._main_frame = Frame(root, name=self._MAIN)  # , bd=1, relief=SUNKEN)
        self._main_frame.grid(row=0, column=0, padx=(10, 10), pady=(20, 20), sticky=N+S+E+W)
        self._main_frame.columnconfigure(0, weight=1)
        self._main_frame.rowconfigure(2, weight=1)

    def setup_children(self) -> "MainFrame":
        SourceDirectory(self._main_frame)
        SourceSelector(self._main_frame)

        ExtensionFilter(self._main_frame)
        ExtensionFilteredSourceSelector(self._main_frame)

        FileView(self._main_frame)

        DestinationDirectory(self._main_frame)
        DestinationSelector(self._main_frame)

        FileToProcessSelector(self._main_frame)

        return self
