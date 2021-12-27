# Creating Buttons

from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text='Look! I clicked a Button!')
    myLabel.pack()


# Creating a Button Widget
myButton = Button(root, text='Click Me!', command=myClick)

# Showing it onto the screen
myButton.pack()

root.mainloop()
