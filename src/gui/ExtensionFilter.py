from tkinter import Frame
from tkinter.ttk import Entry

from gui.templates.LabelEntryCombo import LabelEntryCombo
from libs.DotNotation import get_dot_notation


class ExtensionFilter:

    _FRAME = "file_type_frame"
    _LABEL = "file_type_label"
    _ENTRY = "file_type_entry"

    _EXAMPLE = "Ex: avi, mp4, mkv, etc. Finds all if blank"

    def __init__(self, main_frame: Frame):
        self.ext_filter_labeled_entry = (
            LabelEntryCombo(main_frame, self._FRAME)
            .setup_label("Extension Filter:", self._LABEL)
            .setup_entry(self._ENTRY)
            .set_entry_default_focus_binding("Ex: avi, mp4, mkv, etc. Finds all if blank")
            .grid(row=1, column=0)
        )

    @classmethod
    def get_entry(cls, main_frame: Frame) -> Entry:
        return main_frame.nametowidget(
            get_dot_notation(cls._FRAME, cls._ENTRY)
        )
