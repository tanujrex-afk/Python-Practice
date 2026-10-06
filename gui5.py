from tkinter import filedialog
import tkinter as tk
window=tk.Tk()
file=filedialog.askopenfile()
print(file)
window.mainloop()