from tkinter  import *
from tkinter import ttk
window=Tk()
window.geometry("200x150")
win1= Frame(window)
win1.pack()
langs=["C++","Java","Pytthon","PHP"]
combo=ttk.Combobox(win1,values=langs)
combo.set("pick an option")
combo.pack(padx=5,pady=5)
window.mainloop()