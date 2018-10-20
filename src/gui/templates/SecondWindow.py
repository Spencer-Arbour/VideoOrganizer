from tkinter import Toplevel, Frame, Tk

from gui.templates.UiRootSingleton import UiRootSingleton


class SecondWindow(Toplevel):

    def __init__(self, parent: Tk=None, **kw):
        super().__init__(parent if parent else UiRootSingleton(), **kw)
        self.protocol("WM_DELETE_WINDOW", self._do_nothing)
        self.resizable(False, False)

        self._frame = Frame(self)
        self._frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

        self.transient(parent)
        self.grab_set()

    def _close(self):
        self.destroy()

    @staticmethod
    def _do_nothing():
        pass
