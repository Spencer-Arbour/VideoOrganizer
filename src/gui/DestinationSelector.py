import os
from tkinter import Frame, END

from gui.AskDirectory import DirectorySelector
from gui.DestinationDirectory import DestinationDirectory
from gui.WarningPopUps import use_app_directory
from gui.templates.StandardButton import StandardButton
from lib.DirectoryChecks import is_there_entered_value_that_is_directory


class DestinationSelector:

    def __init__(self, main_frame: Frame):
        self._main_frame = main_frame

        self._src_dir_button = StandardButton(main_frame, text="Browse", command=self._find_dir)\
            .grid(row=4, column=1)

    def _find_dir(self):
        entry = DestinationDirectory.get_entry(self._main_frame)
        entry_value = entry.get()

        if not is_there_entered_value_that_is_directory(entry_value):
            if use_app_directory(entry_value):
                new_dir = DirectorySelector.ask_directory(os.getcwd())

            else:
                return

        else:
            new_dir = DirectorySelector.ask_directory(entry_value or os.getcwd())

        if new_dir:
            entry.delete(0, END)
            entry.insert(0, new_dir)
