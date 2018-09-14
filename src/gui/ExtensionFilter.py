from tkinter import Frame, END
from tkinter.ttk import Entry

from gui.templates.LabelEntryCombo import LabelEntryCombo
from lib.DotNotation import get_dot_notation


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
            .grid(row=1, column=0)
        )
        self._setup_entry_binding(self.ext_filter_labeled_entry.entry)
        self._entry_get_override(self.ext_filter_labeled_entry.entry)


    @classmethod
    def get_entry(cls, main_frame: Frame) -> Entry:
        return main_frame.nametowidget(
            get_dot_notation(cls._FRAME, cls._ENTRY)
        )

    def _setup_entry_binding(self, entry: Entry):
        entry.insert(0, self._EXAMPLE)
        entry.config(fg="grey")

        def focus_in(event):
            if entry.tk.call(entry._w, 'get') == self._EXAMPLE:
                entry.delete(0, END)
                entry.insert(0, "")
                entry.config(fg="black")

        def focus_out(event):
            if entry.tk.call(entry._w, 'get') == "":
                entry.delete(0, END)
                entry.insert(0, self._EXAMPLE)
                entry.config(fg="grey")

        entry.bind("<FocusIn>", focus_in)
        entry.bind("<FocusOut>", focus_out)

    def _entry_get_override(self, entry: Entry):

        def new_get():
            val = entry.tk.call(entry._w, "get")
            if val == self._EXAMPLE:
                return ""
            return val

        entry.get = new_get


