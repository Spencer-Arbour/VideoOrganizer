from tkinter import Label

from gui.templates.SecondWindow import SecondWindow
from gui.templates.StandardButton import StandardButton


class Info(SecondWindow):

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)

        information = Label(self._frame,
                            text="Brought to you by me\n"
                                 "This is where the thank you would go for the online db and such\n"
                                 "This is where the license agreement goes"
                            )
        information.grid(row=0, column=0)

        StandardButton(self._frame, text="Ok", command=self._close).grid(row=1, column=0, pady=(10, 0))
