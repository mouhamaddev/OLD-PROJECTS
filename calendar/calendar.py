
from tkinter import *

import calendar

root = Tk()

root.title("My Own Gui Calendar")

year = 2020

myCal = calendar.calendar(year)

cal_year = Label(root, text=myCal, font="Consolas 10 bold")

cal_year.pack()

root.mainloop()
