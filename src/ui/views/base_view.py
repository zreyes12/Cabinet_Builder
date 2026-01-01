import tkinter as tk

class BaseView(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

    def pack(self, *args, **kwargs):
        raise RuntimeError(
            f"{self.__class__.__name__} must not call pack() — "
            "ViewManager controls layout."
        )

    def place(self, *args, **kwargs):
        raise RuntimeError(
            f"{self.__class__.__name__} must not call place()."
        )