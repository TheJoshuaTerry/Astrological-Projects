from tkinter import *
from Code import *
#from Horoscope import *

root = Tk()
# Creating a Label widget
header1 = Label(root, text='Since you were born in the year')
header2 = Label(root, text=year)
header3 = Label(root, text='your Zodiac animal is the')
header4 = Label(root, text='and given that you were born on the')
header5 = Label(root, text=days)
header6 = Label(root, text='of')
header7 = Label(root, text=mon)
header8 = Label(root, text='You star sign is')
myLabel1 = Label(root, text=zodiac(year))
myLabel2 = Label(root, text=horoscope(month, day))
#Putting it on the screen
header1.grid(row=0, column=1)
header2.grid(row=1, column=1)
header3.grid(row=2, column=1)
myLabel1.grid(row=4, column=1)

header4.grid(row=6, column=1)
header5.grid(row=7, column=1)
header6.grid(row=8, column=1)
header7.grid(row=9, column=1)
header8.grid(row=10, column=1)
myLabel2.grid(row=11, column=1)
root.mainloop()