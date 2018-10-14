from tkinter import Tk


class UiRootSingleton:

    _root = None

    def __new__(cls, *args, **kwargs):
        if not cls._root:
            cls._root = Tk()

        return cls._root
