import time
import customtkinter as ctk
from typing import Callable

class Animator:
    @staticmethod
    def fade_in(widget: ctk.CTkBaseClass, duration=0.5):
        widget.configure(state="disabled")
        for i in range(0, 101, 5):
            alpha = i/100
            widget.attributes('-alpha', alpha)
            widget.update()
            time.sleep(duration/20)
        widget.configure(state="normal")

    @staticmethod
    def slide_in(widget: ctk.CTkBaseClass, direction="left", duration=0.3):
        original_pos = widget.winfo_x()
        if direction == "left":
            widget.place(x=-widget.winfo_width(), y=widget.winfo_y())
        elif direction == "top":
            widget.place(y=-widget.winfo_height(), x=widget.winfo_x())
        
        steps = 20
        for i in range(steps + 1):
            if direction == "left":
                new_x = original_pos - (original_pos + widget.winfo_width()) * (1 - i/steps)
                widget.place(x=new_x)
            elif direction == "top":
                new_y = widget.winfo_y() - widget.winfo_height() * (1 - i/steps)
                widget.place(y=new_y)
            widget.update()
            time.sleep(duration/steps)