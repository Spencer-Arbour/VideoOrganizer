from gui.templates.SecondWindow import SecondWindow
from gui.templates.StandardButton import StandardButton


class ShowChooser(SecondWindow):

    def __init__(self, shows=None, **kw):
        super().__init__(**kw)

        self._shows = shows
        self._show_id = None

        for index, show in enumerate(shows):
            StandardButton(self).grid(column=0, row=index)

    def _select_id(self, index):
        self._shows[index].get("id")
