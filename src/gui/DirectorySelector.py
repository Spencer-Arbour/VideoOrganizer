from tkinter import Entry, filedialog, messagebox, END
import os
from typing import Union


class DirectorySelector:


    @classmethod
    def get_directory(cls, entry: Entry) -> None:
        valid_initial_dir = cls._get_valid_initial_dir(entry.get())

        if valid_initial_dir:
            new_dir = filedialog.askdirectory(initialdir=valid_initial_dir)

            if not new_dir:
                return

            entry.delete(0, END)
            entry.insert(0, new_dir)


    @staticmethod
    def _get_valid_initial_dir(directory: str) -> Union[str, bool]:

        if not directory:
            return os.getcwd()

        elif os.path.isdir(directory):
            return directory

        elif messagebox.askokcancel(
                "Invalid Directory", "Directory does not exist: \n{}\n Would you like to "
                                     "start searching from the video organizer location?".format(directory)
        ):
            return "/"

        else:
            return False
