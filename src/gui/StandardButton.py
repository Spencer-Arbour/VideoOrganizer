from tkinter import Button


class StandardButton(Button):
    _WIDTH = 10

    def __init__(self, master, **kw):
        super().__init__(master, **kw)

    def grid(self, **kw) -> "StandardButton":
        super().grid(**kw)
        return self
