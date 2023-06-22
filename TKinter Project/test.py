from tkinter import *


"""
text_label = Label(root, text="BONJ")

text_label.pack(padx=20, pady=20)

text_entry = Entry(root)
text_box = Text(root, height=5)
text_box.pack(padx=30)
btn1 = Button(root, text= "press this button")
btn1.pack(padx=15, pady=15)

check_btn1 = Checkbutton(root)
check_btn1.pack()

todo_frame = Frame(root)
todo_frame.columnconfigure(0, weight=1)
todo_frame.columnconfigure(1, weight=1)
todo_frame.columnconfigure(2, weight=1)
todo_frame.columnconfigure(3 , weight=1)

box_1 = Button(todo_frame, text= "1")
box_1.grid(row=0, column=0, sticky=W+E)

box_2 = Button(todo_frame, text= "2")
box_2.grid(row=0, column=1, sticky=W+E)


todo_frame.pack(fill="x", padx= 20)
"""
class test_GUI:
    def __init__(self):
        self.root = Tk()
        self.label = Label(self.root, text="E")
        self.label.pack(padx=20, pady=20)

        self.textbox = Text(self.root, height=4)
        self.textbox.pack(padx=10, pady=10)
        self.check = Checkbutton(self.root, text="show")
        self.check.pack(padx= 10, pady=10)
        self.root.mainloop()

test_GUI()

"""TUTORIAL:
Tkinter Beginner Course - Python GUI Development
Minute: 21:45
https://youtu.be/ibf5cx221hk


"""

