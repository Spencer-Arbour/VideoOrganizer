from tkinter import Frame, Label, Entry, E, W, END


class LabelEntryCombo:


    def __init__(self, container: Frame, name: str=None):
        self._frame = Frame(container, name=name)
        self._frame.columnconfigure(1, weight=1)

        self._entry = None
        self._entry_name = None
        self._label_name = None

    @property
    def entry(self):
        return self._entry

    def setup_label(self, label_text: str, name: str=None) -> "LabelEntryCombo":
        self._label_name = name

        label = Label(self._frame, text=label_text, name=name, width=15)
        label.grid(row=0, column=0)

        label.bind("Alt-")

        return self

    def setup_entry(self, name: str=None, default_entry: str="", width: int=50) -> "LabelEntryCombo":
        self._entry_name = name

        self._entry = Entry(self._frame, name=name, width=width)
        self._entry.grid(row=0, column=1, sticky=E + W)
        self._entry.columnconfigure(0, weight=1)
        self._entry.insert(0, default_entry)

        # def select_all(event):
        #     event.widget.select_range(0, END)
        #     event.widget.icursor(END)

        # self._entry.bind("<Command-KeyRelease-a>", select_all)  # todo - this will need to change for windows

        return self

    def grid(self, **kw) -> "LabelEntryCombo":
        if not kw.get("sticky", False):
            kw["sticky"] = E+W

        self._frame.grid(**kw)

        return self

    def _alt_code(self):
        pass
