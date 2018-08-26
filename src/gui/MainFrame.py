from tkinter import Frame, Label, Entry, Button, SUNKEN, E, W, N, S

from gui.DirectorySelector import DirectorySelector


class MainFrame:

    def __init__(self, container):
        self._root = container

        self._main_frame = Frame(container)  # , bd=1, relief=SUNKEN)
        self._main_frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky=N+S+E+W)
        self._main_frame.columnconfigure(0, weight=1)

        self._src_dir = SourceDirectory(self._main_frame)


class SourceDirectory:

    def __init__(self, container):
        self._container = container

        self._src_dir_level_entry = LabelEntryCombo(self._container, "Source Directory").grid(row=0, column=0)

        self._src_dir_button = Button(
            self._container, width=10, text="Browse",
            command=lambda: DirectorySelector.get_directory(self._src_dir_level_entry.entry)
        )
        self._src_dir_button.grid(row=0, column=1)


class LabelEntryCombo:

    def __init__(self, container, label_text: str, default_entry: str=""):
        self._frame = Frame(container)
        self._frame.columnconfigure(1, weight=1)

        self._label = Label(self._frame, text=label_text, width=15)
        self._label.grid(row=0, column=0)

        self.entry = Entry(self._frame, width=50)
        self.entry.grid(row=0, column=1, sticky=E + W)
        self.entry.columnconfigure(0, weight=1)
        self.entry.insert(0, default_entry)

    def grid(self, **kw) -> "LabelEntryCombo":
        if not kw.get("sticky", False):
            kw["sticky"] = E+W
        self._frame.grid(**kw)
        return self
