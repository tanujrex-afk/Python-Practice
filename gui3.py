import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
def show_msg():
    messagebox.showinfo(
        "information","welcome to python"
    )
button=tk.Button(
    window,text="click",command=show_msg
)
button.pack()
window.mainloop()