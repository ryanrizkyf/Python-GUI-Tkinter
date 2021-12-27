# Creating Input Fields

from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, 'Enter Your Name: ')


def myClick():
    hello = 'Hello ' + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


# Creating a Button Widget
myButton = Button(root, text='Enter Your Name', command=myClick)

# Showing it onto the screen
myButton.pack()

root.mainloop()
