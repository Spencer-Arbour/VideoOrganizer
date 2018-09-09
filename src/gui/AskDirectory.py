from tkinter import filedialog


class DirectorySelector:


    @classmethod
    def ask_directory(cls, starting_directory: str) -> str:
        return filedialog.askdirectory(initialdir=starting_directory)
