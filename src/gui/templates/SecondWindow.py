from tkinter import Toplevel, Frame, Tk

from gui.templates.UiRootSingleton import UiRootSingleton


class SecondWindow(Toplevel):

    def __init__(self, parent: Tk=None, **kw):
        super().__init__(parent if parent else UiRootSingleton, **kw)
        self.resizable(False, False)
        self.overrideredirect(1)
        self._frame = Frame(self)
        self._frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))


        self.transient(parent)
        self.grab_set()

    def _close(self):
        self.destroy()