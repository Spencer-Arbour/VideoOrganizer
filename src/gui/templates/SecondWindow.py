from tkinter import Toplevel, Frame, Tk


class SecondWindow(Toplevel):

    def __init__(self, parent: Tk, **kw):
        super().__init__(parent, **kw)
        self.resizable(False, False)

        self.transient(parent)
        self.grab_set()

        self._frame = Frame(self)
        self._frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

    def _close(self):
        self.destroy()