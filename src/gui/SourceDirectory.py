from tkinter import Frame

from gui.templates.LabelEntryCombo import LabelEntryCombo
from lib.DotNotation import get_dot_notation


class SourceDirectory:

    _FRAME = "src_dir_frame"
    _LABEL = "src_dir_label"
    _ENTRY = "src_dir_entry"

    def __init__(self, main_frame: Frame):
        self._src_dir_labeled_entry = (
            LabelEntryCombo(main_frame, self._FRAME)
            .setup_label("Source Directory:", self._LABEL)
            .setup_entry(self._ENTRY)
            .grid(row=0, column=0)
        )

    @classmethod
    def get_entry(cls, main_frame: Frame):
        return main_frame.nametowidget(
            get_dot_notation(cls._FRAME, cls._ENTRY)
        )



