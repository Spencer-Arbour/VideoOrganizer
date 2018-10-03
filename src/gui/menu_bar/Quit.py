from tkinter import Tk, Label

from gui.templates.SecondWindow import SecondWindow
from gui.templates.StandardButton import StandardButton


class Quit(SecondWindow):

    def __init__(self, parent: Tk, **kw):
        super().__init__(parent, **kw)
        self._parent = parent

        Label(self._frame, text="Are you sure you want to quit VideoOrganizer?").grid(row=0, column=0, columnspan=2)

        StandardButton(self._frame, text="Cancel", command=self._close).grid(row=1, column=0)
        StandardButton(self._frame, text="Quit", command=self._quit).grid(row=1, column=1)

    def _quit(self):
        self._parent.quit()
        self._parent.destroy()
        quit()
