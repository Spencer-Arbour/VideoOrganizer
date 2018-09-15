from tkinter import Frame, Label, Entry, E, W, END


class LabelEntryCombo:


    def __init__(self, container: Frame, name: str):
        self._frame = Frame(container, name=name)
        self._frame.columnconfigure(1, weight=1)

        self._entry = None
        self._entry_name = None
        self._label_name = None

    def setup_label(self, label_text: str, name: str) -> "LabelEntryCombo":
        self._label_name = name

        label = Label(self._frame, text=label_text, name=name, width=15)
        label.grid(row=0, column=0)

        return self

    def setup_entry(self, name: str, default_entry: str="") -> "LabelEntryCombo":
        self._entry_name = name

        self._entry = Entry(self._frame, name=name, width=50)
        self._entry.grid(row=0, column=1, sticky=E + W)
        self._entry.columnconfigure(0, weight=1)
        self._entry.insert(0, default_entry)

        return self


    def set_entry_default_focus_binding(self, default: str) -> "LabelEntryCombo":
        self._entry.insert(0, default)
        self._entry.config(fg="grey")

        # noinspection PyUnusedLocal,PyProtectedMember
        def focus_in(event):
            if self._entry.tk.call(self._entry._w, 'get') == default:
                self._entry.delete(0, END)
                self._entry.insert(0, "")
                self._entry.config(fg="black")

        # noinspection PyUnusedLocal,PyProtectedMember
        def focus_out(event):
            if self._entry.tk.call(self._entry._w, 'get') == "":
                self._entry.delete(0, END)
                self._entry.insert(0, default)
                self._entry.config(fg="grey")

        # noinspection PyProtectedMember
        def new_get():
            val = self._entry.tk.call(self._entry._w, "get")
            if val == default:
                return ""
            return val

        self._entry.bind("<FocusIn>", focus_in)
        self._entry.bind("<FocusOut>", focus_out)
        self._entry.get = new_get

        return self

    def grid(self, **kw) -> "LabelEntryCombo":
        if not kw.get("sticky", False):
            kw["sticky"] = E+W

        self._frame.grid(**kw)

        return self
