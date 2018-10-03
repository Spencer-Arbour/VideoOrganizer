from tkinter import Tk

from gui.menu_bar.MenuBar import MenuBar
from src.gui.MainFrame import MainFrame


class VideoOrganizer:

    def __init__(self):
        self._root = Tk()
        self._root.title("Video Organizer")
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)

    def create_menu_bar(self) -> "VideoOrganizer":
        MenuBar(self._root)
        return self

    def create_main_frame(self) -> "VideoOrganizer":
        MainFrame(self._root).setup_children()
        return self

    def start(self) -> "VideoOrganizer":
        self._root.mainloop()
        return self


if __name__ == "__main__":
    VideoOrganizer()\
        .create_menu_bar()\
        .create_main_frame()\
        .start()
