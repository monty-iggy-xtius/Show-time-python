import tkinter
import random
import time
from tkinter import Label


min_width, min_height = 375, 80
clock_window = tkinter.Tk()
clock_window.config(bg="black")
clock_window.title("yuri clock")
clock_window.iconbitmap("logo/logo.ico")
clock_window.geometry('380x80')
clock_window.minsize(min_width, min_height)
clock_window.resizable(False, False)

colors = ['blue', 'cyan', 'spring green2', 'lime', 'magenta', 'pink', 'navyblue', 'purple']
clock_label = Label(clock_window, font=("IGES 1001", 50, 'bold'), background='black', foreground=random.choice(colors))
clock_label.pack(anchor='center')


def get_time():
	current_time = time.strftime("%H: %M: %S")
	clock_label.config(text=current_time)
	clock_label.after(1000, get_time)


if __name__ == '__main__':
	get_time()
	clock_window.mainloop()