from tkinter import Frame, Label, Entry, E, W


class LabelEntryCombo:


    def __init__(self, container: Frame, name: str):
        self._frame = Frame(container, name=name)
        self._frame.columnconfigure(1, weight=1)

        self.entry = None
        self._entry_name = None
        self._label_name = None

    def setup_label(self, label_text: str, name: str) -> "LabelEntryCombo":
        self._label_name = name

        label = Label(self._frame, text=label_text, name=name, width=15)
        label.grid(row=0, column=0)

        return self

    def setup_entry(self, name: str, default_entry: str="") -> "LabelEntryCombo":
        self._entry_name = name

        self.entry = Entry(self._frame, name=name, width=50)
        self.entry.grid(row=0, column=1, sticky=E + W)
        self.entry.columnconfigure(0, weight=1)
        self.entry.insert(0, default_entry)

        return self

    def grid(self, **kw) -> "LabelEntryCombo":
        if not kw.get("sticky", False):
            kw["sticky"] = E+W

        self._frame.grid(**kw)

        return self
