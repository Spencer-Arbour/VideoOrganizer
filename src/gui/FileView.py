from tkinter import W, E, S, N, NO, CENTER
from tkinter.ttk import Treeview

<<<<<<< HEAD
from libs.DotNotation import get_dot_notation
=======
from lib.DotNotation import get_dot_notation
from lib.FileGetter import get_files
>>>>>>> feature/get_file_info


class FileView(Treeview):
    # todo replace with custom widget that does stuff like checkboxes and embedded drop downs
    _TREE_VIEW = "file_tree_view"

    _NOT_SELECTED = "□"
    _SELECTED = "▣"

    _C1 = "#1"
    _C2 = "#2"
    _C3 = "#3"

    _IS_ALL_SELECTED = False
    _SWITCHER = {False: _SELECTED, True: _NOT_SELECTED}

    _ODD = "odd_row"
    _EVEN = "even_row"

    _SRC = 2
    _NAME = 1

    def __init__(self, main_frame):
        super().__init__(main_frame, columns=("Selected", "File", "Directory"), name=self._TREE_VIEW, show="headings")

        self.heading(self._C1, text="□", command=self._select_all_toggle, anchor=CENTER)
        self.column(self._C1, minwidth=30, width=30, stretch=NO, anchor=CENTER)

        self.heading(self._C2, text="File")
        self.heading(self._C3, text="Directory")
        self.grid(row=2, column=0, columnspan=2, pady=(20, 20), sticky=E + W + N + S)
        self.bind("<Button-1>", self._on_item_click)

    @classmethod
    def get_fileview(cls, main_frame):
        return main_frame.nametowidget(
            get_dot_notation(cls._TREE_VIEW)
        )

<<<<<<< HEAD
    def set_files(self, files: tuple):
        self._delete_all_children()
        self.heading(self._C1, text=self._NOT_SELECTED)

        for key, value in files:
            self.insert("", "end", values=[self._NOT_SELECTED, value, key])
=======
    def set_files(self, files: get_files):
        self._delete_all_children()
        self.heading(self._C1, text=self._NOT_SELECTED)

        for src, name in files:
            self.insert("", "end", values=[self._NOT_SELECTED, name, src])
>>>>>>> feature/get_file_info

    def get_files(self):
        for child in self.get_children():
            value = self.item(child)["values"]
            if value[0] == self._SELECTED:
                yield value[self._SRC],  value[self._NAME]

    def _on_item_click(self, event):
        # todo - find a way to only set if C1 is clicked and remove highlighting
        child = self.identify("item", event.x, event.y)
        if self.item(child)["values"] == "":
            return

        if self.item(child)["values"][0] == self._SELECTED:
            self.set(child, self._C1, self._NOT_SELECTED)
            self.heading(self._C1, text=self._NOT_SELECTED)

        else:
            self.set(child, self._C1, self._SELECTED)
            if self._all_selected():
                self.heading(self._C1, text=self._SELECTED)

    def _all_selected(self):
        for child in self.get_children():
            if self.item(child)["values"][0] == self._NOT_SELECTED:
                return False
        return True

    def _select_all_toggle(self):
        if self.heading(self._C1)["text"] == self._SELECTED:
            self._toggle_all(self._NOT_SELECTED)

        else:
            self._toggle_all(self._SELECTED)

    def _toggle_all(self, toggle_val):
        self.heading(self._C1, text=toggle_val)

        for item in self.get_children():
            self.set(item, self._C1, toggle_val)

    def _delete_all_children(self):
        self.delete(*self.get_children())
