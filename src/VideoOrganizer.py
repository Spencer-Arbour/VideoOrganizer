from tkinter import Tk

from src.gui.MainFrame import MainFrame


class VideoOrganizer:

    def __init__(self):
        self._root = Tk()
        self._root.columnconfigure(0, weight=1)

    def create_main_frame(self) -> "VideoOrganizer":
        MainFrame(self._root)
        return self

    def start(self) -> "VideoOrganizer":
        self._root.mainloop()
        return self


if __name__ == "__main__":
    VideoOrganizer()\
        .create_main_frame()\
        .start()
