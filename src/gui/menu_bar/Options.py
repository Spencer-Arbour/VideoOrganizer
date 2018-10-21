from tkinter import E, W

from gui.menu_bar.Config import Config
from gui.templates.LabelEntryCombo import LabelEntryCombo
from gui.templates.SecondWindow import SecondWindow
from gui.templates.StandardButton import StandardButton


class Options(SecondWindow):

    _ENTRY_WIDTH = 30

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self._name = LabelEntryCombo(self._frame).setup_label("Username")\
            .setup_entry(width=self._ENTRY_WIDTH)\
            .grid(row=0, column=0, columnspan=2)

        self._foo = LabelEntryCombo(self._frame).setup_label("Unique ID")\
            .setup_entry(width=self._ENTRY_WIDTH)\
            .grid(row=1, column=0, columnspan=2)

        self._bar = LabelEntryCombo(self._frame).setup_label("API Key")\
            .setup_entry(width=self._ENTRY_WIDTH)\
            .grid(row=2, column=0, columnspan=2)

        StandardButton(self._frame, text="Cancel", command=self._close)\
            .grid(row=3, column=0, padx=(40, 0), pady=(10, 0), sticky=W)

        StandardButton(self._frame, text="Ok", command=self._ok)\
            .grid(row=3, column=1, padx=(0, 40), pady=(10, 0), sticky=E)


    def _ok(self):
        Config.NAME = self._name.entry.get()
        Config.FOO = self._foo.entry.get()
        Config.BAR = self._bar.entry.get()

        self._close()
