from tkinter import Button


class StandardButton(Button):
    _WIDTH = "width"
    _WIDTH_VAL = 10

    def __init__(self, master, **kw):
        if not kw.get(self._WIDTH, None):
            kw[self._WIDTH] = self._WIDTH_VAL
        super().__init__(master, **kw)

    def grid(self, **kw) -> "StandardButton":
        super().grid(**kw)
        return self
