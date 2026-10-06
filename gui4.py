import tkinter as tk
from tkinter.simpledialog import askstring
window=tk.Tk()
name=askstring("input","Enter your namme")
print(name)
window.mainloop()