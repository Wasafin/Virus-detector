# import all the neccesary libraries'
from tkinter import *
from tkinter import messagebox

# setup Tkinter window
window = Tk()
window.geometry("200x200")

# funstion for displaying warning message
# this will be called once the button is clicked

def msg():
    messagebox.askokcancel("Alert!", "Stop! VIRUS FOUND!")

# adding button widget to window
b1 = Button(window, text="Scan for Virus", command=msg)
b1.pack()

# entering main event loop
window.mainloop()