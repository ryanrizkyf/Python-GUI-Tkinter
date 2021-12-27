# Using Icons, Images, and Exit Buttons

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Belajar GUI')
# root.iconbitmap('images/LogoGunadarma.ico')

my_img = ImageTk.PhotoImage(Image.open(
    'images/photo-2.jpg'))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()

root.mainloop()
