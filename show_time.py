import tkinter as tk
import random
import time
import sys
import pyglet

MIN_WIDTH: int = 380
MIN_HEIGHT: int = 80
TITLE: str = "yuri clock"
BACKGROUND: str = "black"
FOREGROUND_COLORS: list[str] = ['blue', 'cyan', 'spring green',
                     'lime', 'magenta', 'pink', 'navyblue', 'purple']

# load the custom font file
pyglet.font.add_file("./fonts/custom.ttf")

clock_window = tk.Tk()
clock_window.config(bg=BACKGROUND)
clock_window.title(TITLE)
clock_window.geometry("385x80")
clock_window.resizable(False, False)
clock_window.minsize(MIN_WIDTH, MIN_HEIGHT)
if "win" in sys.platform:
    clock_window.iconbitmap("logo/logo.ico")

clock_label = tk.Label(
	master=clock_window, 
	font=("custom", 46),
	background=BACKGROUND, 
	foreground=random.choice(FOREGROUND_COLORS))
clock_label.place(relx=0.5, rely=0.5, anchor="center")


def get_time() -> None:
    """
    This function updates the time label after every second.
    """
    # current time format to be displayed on the label
    current_time = time.strftime("%H : %M : %S")
    clock_label.configure(text=current_time)
    clock_label.after(1000, get_time)


if __name__ == '__main__':
    get_time()
    clock_window.mainloop()