import tkinter as tk
from tkinter import messagebox

class test_GUI:
    def __init__(self):
        self.root = tk.Tk()
        
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close this weird program", command= exit)

        self.menubar.add_cascade(menu=self.filemenu, label="File I guess?")

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="E")
        self.label.pack(padx=20, pady=20)

        self.textbox = tk.Text(self.root, height=4)
        self.textbox.bind("<KeyPress>", self.shortcut)
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
    def shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            self.show_message()
    
    def shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            print("H")
    def on_closing(self):
        messagebox.showinfo(title="Message", message="Bye byeee")
        self.root.destroy()

test_GUI()

"""TUTORIAL:
Tkinter Beginner Course - Python GUI Development
Minute: 21:45
https://youtu.be/ibf5cx221hk


"""

