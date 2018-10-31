from tkinter import Label

from gui.templates.SecondWindow import SecondWindow
from gui.templates.StandardButton import StandardButton


class TvDbConnProblem(SecondWindow):

    def __init__(self, **kw):
        super().__init__(**kw)
        self._process = None

        Label(self._frame, text="There was a problem connecting to the TvDb.\n"
                                "Would you like to process the tv files without\n"
                                "attempting to retrieve episode names?"
              ).grid(row=0, column=0, columnspan=2)

        StandardButton(self._frame, text="Cancel", command=self._close).grid(row=1, column=0)
        StandardButton(self._frame, text="Ok", command=self._ok).grid(row=1, column=1)

    @property
    def process(self):
        return self._process

    def _ok(self):
        self._process = True
        self._close()
