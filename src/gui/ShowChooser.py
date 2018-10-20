from tkinter import Label, LEFT, W, Frame
from typing import Tuple

from gui.templates.SecondWindow import SecondWindow
from gui.templates.StandardButton import StandardButton


class ShowChooser(SecondWindow):

    def __init__(self, search, shows, **kw):
        super().__init__(**kw)

        self._shows = shows
        self._show = None

        self._header(search)
        self._body(shows)
        self._footer()

    @property
    def show(self):
        return self._show

    def _select_id(self, index):
        self._show = self._shows[index]
        self._close()

    def _header(self, search: str):
        Label(self._frame,
              text="Multiple series matched the "
                   "search for: \"{}\". Please select "
                   "the appropriate series".format(search),
              wraplength=400
              ).grid(row=0, column=0)

    def _body(self, shows: list):
        container = Frame(self._frame)
        container.grid(row=1, column=0, pady=(10, 10), padx=(10, 10))

        offset = 0
        for index, show in enumerate(shows):

            StandardButton(container, text="Select", command=lambda i=index: self._select_id(i)) \
                .grid(column=0, row=index + offset)

            Label(
                container,
                text=self._trim_overview(show.get("overview", None)),
                wraplength=500,
                justify=LEFT
            ).grid(column=1, row=index + offset, sticky=W, padx=(10, 0), pady=(10, 10))

    def _footer(self) -> None:
        StandardButton(self._frame, text="Skip", command=self._close).grid(row=2, column=0)


    @staticmethod
    def _trim_overview(overview: str, trim_len=None) -> str:
        dots = "..."

        if (not trim_len) or trim_len < 0:
            trim_len = 200

        if len(overview) > trim_len:
            return overview[:trim_len - len(dots)] + dots

        return overview
