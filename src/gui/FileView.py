from tkinter import W, E, S, N, NO, CENTER
from tkinter.ttk import Treeview

from lib.DotNotation import get_dot_notation


class FileView(Treeview):
    _TREE_VIEW = "file_tree_view"

    _NOT_SELECTED = "□"
    _SELECTED = "▣"

    _ALL_SELECTED = False
    _SWITCHER = {False: _SELECTED, True: _NOT_SELECTED}

    _ODD = "odd_row"
    _EVEN = "even_row"

    def __init__(self, main_frame):
        super().__init__(main_frame, columns=("Selected", "File", "Directory"), name=self._TREE_VIEW, show="headings")

        self.heading("#1", text="□", command=self.select_all_toggle, anchor=CENTER)
        self.column("#1", minwidth=30, width=30, stretch=NO, anchor=CENTER)

        self.heading("#2", text="File")
        self.heading("#3", text="Directory")
        self.grid(row=2, column=0, columnspan=2, pady=(10, 10), sticky=E + W + N + S)
        
        
        # todo
        # self.tag_configure(self._ODD, background="white")
        # self.tag_configure(self._EVEN, background="grey90")

    @classmethod
    def get_fileview(cls, main_frame):
        return main_frame.nametowidget(
            get_dot_notation(cls._TREE_VIEW)
        )

    def select_all_toggle(self):
        self.heading("#0", text=self._SWITCHER[self._ALL_SELECTED])
        self._ALL_SELECTED = not self._ALL_SELECTED


    def add_files(self, files: dict):
        self._delete_all_children()

        for key, values in files.items():
            for iterator, value in enumerate(values):

                self.insert(
                    "", "end", values=[self._NOT_SELECTED, value, key],
                    # tags=((self._ODD,) if iterator % 2 == 0 else (self._EVEN,))
                )

    def _delete_all_children(self):
        self.delete(*self.get_children())
