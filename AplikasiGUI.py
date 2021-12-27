from tkinter import *

window = Tk()
window.title('GUI Skripsi')
window.geometry("600x500")

label = Label(
    window,
    text="Analisis dan Prediksi Kasus COVID-19\nASEAN, Dunia, dan Indonesia",
    font=('Arial Bold', 16))
label.pack()

btn = Button(window, text="This is Button widget", fg='blue')
btn.place(x=80, y=100)

# You will first create a division with the help of Frame class and align them on TOP and BOTTOM with pack() method.
# top_frame = Frame(window).pack()
# bottom_frame = Frame(window).pack(side="bottom")

# Once the frames are created then you are all set to add widgets in both the frames.
# 'fg or foreground' is for coloring the contents (buttons)
# btn1 = Button(top_frame, text="Button1", fg="red").pack()

# btn2 = Button(top_frame, text="Button2", fg="green").pack()

# btn3 = Button(bottom_frame, text="Button3", fg="purple").pack(
#    side="left")  # 'side' is used to left or right align the widgets

# btn4 = Button(bottom_frame, text="Button4",
#              fg="orange").pack(side="left")

scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)

Lb1 = Listbox(window)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.pack()

window.mainloop()
