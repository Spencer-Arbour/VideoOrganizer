from tkinter import Tk, Menu
from tkinter.messagebox import _show


class MenuBar:

    def __init__(self, root: Tk):
        self._root = root

        menu_bar = Menu(self._root)
        self._root.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Options")
        file_menu.add_command(label="Exit", command=self._quit)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Info", command=self._info)

        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def _options(self):
        pass

    def _quit(self):
        self._root.quit()
        self._root.destroy()
        exit()

    def _info(self):
        _show("", "None")
