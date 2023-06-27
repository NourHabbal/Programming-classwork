import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

"""
Note: This is based off the given tutorial: https://youtu.be/ibf5cx221hk
The theme used is the forest theme by rdbende: https://github.com/rdbende/Forest-ttk-theme


"""


class test_GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close This Weird Program", command= exit)
        self.filemenu.add_command(label="Do something I guess", command= self.do_something)
        self.filemenu.add_command(label="Do something else", command=self.do_something_else)

        #self.root.tk.call('source', 'forest-dark.tcl')
        #self.style = ttk.Style(self.root)
# Set the theme with the theme_use method
        #self.style.theme_use('forest-dark')

        self.menubar.add_cascade(menu=self.filemenu, label="Some Menu")

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="Tkinter GUI Test Project")
        self.label.pack(padx=20, pady=20)

        self.text = tk.Label(self.root, height= 3, text= "\n\nDirections for this test project: \n 1. Write in the textbox, and press the button below, which will create a popup of what you wrote. \nIf you want ypur message to appear in the terminal, toggle the checkbox.")
        self.text.pack(padx=10,pady=10)

        self.text2= tk.Label(self.root, height= 3, text="This is a practice project I made while messing around with TKinter's features." )
        self.text2.pack(padx=10,pady=10)

        self.textbox = tk.Text(self.root, height=4)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        
        self.check = tk.Checkbutton(self.root, text="display in terminal", variable= self.check_state)
        self.check.pack(padx= 10, pady=10)

        self.button = tk.Button(self.root, text="show text content as message", command= self.show_message)
        self.button.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def show_message(self):
        if (self.check_state.get()):
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))
    #def shortcut(self, event):
    #    if event.state == 12 and event.keysym == "Return":
    #        self.show_message()
    
    def on_closing(self):
        messagebox.showinfo(title="message", message="bye-bye")
        self.root.destroy()
    def do_something(self):
        messagebox.showinfo(title="Pun", message="my dog ate my homework")
        messagebox.showinfo(title="Pun", message="some lad on the internet: then it must've took him a couple bytes")
    def do_something_else(self):
        messagebox.showerror(title="?", message="the statement below is False\n\nthe statement above is True")

test_GUI()
