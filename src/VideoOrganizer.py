from tkinter import Tk


class VideoOrganizer:

    def __init__(self):
        self._root = Tk()

    def start(self):
        self._root.mainloop()


if __name__ == "__main__":
    VideoOrganizer().start()
