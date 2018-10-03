from tkinter import Tk, Menu
from gui.menu_bar.Info import Info
from gui.menu_bar.Options import Options
from gui.menu_bar.Quit import Quit


class MenuBar:

    def __init__(self, root: Tk):
        self._root = root

        menu_bar = Menu(self._root)
        self._root.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Options", command=self._options)
        file_menu.add_command(label="Quit", command=self._quit)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Info", command=self._info)

        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def _options(self):
        Options(self._root)

    def _quit(self):
        Quit(self._root)

    def _info(self):
        Info(self._root)

