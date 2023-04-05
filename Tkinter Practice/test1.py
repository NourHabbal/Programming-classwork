
from tkinter import *
from tkinter import ttk

import sv_ttk

root = Tk()
title = ttk.Entry(root,text="hi")
title.place(rely=0.05,relx=0.345)

paragraph = ttk.Button(root,text="hrhjegrjhejrjhegherghefrefgeejehgfejgrhegrherhjereghfrehfherktklttjtpotgklhgjhklgjkri")
paragraph.place(rely=0.1,relx=0.100)

button = ttk.Label(root,text="hi")
button.place(relx=2.0, rely=4.0)




root.geometry("1080x720")
sv_ttk.set_theme("dark")
root.mainloop()