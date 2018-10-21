from tkinter import Frame

from gui.templates.LabelEntryCombo import LabelEntryCombo
from libs.DotNotation import get_dot_notation


class DestinationDirectory:

    _FRAME = "dest_dir_frame"
    _LABEL = "dest_dir_label"
    _ENTRY = "dest_dir_entry"

    def __init__(self, main_frame: Frame):
        self._src_dir_labeled_entry = (
            LabelEntryCombo(main_frame, self._FRAME)
            .setup_label("Destination Directory:", self._LABEL)
            .setup_entry(self._ENTRY)
            .grid(row=4, column=0)
        )

    @classmethod
    def get_entry(cls, main_frame: Frame):
        return main_frame.nametowidget(
            get_dot_notation(cls._FRAME, cls._ENTRY)
        )



