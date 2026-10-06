import tkinter as tk
from tkinter import ttk
import time
root=tk.Tk()
def start_progress():
    progress.start()
    for i in range(101):
        time.sleep(0.06)
        progress['value']= i
        root.update_idletasks()
    progress.stop()
root.title("Progress bar example")
progress=ttk.Progressbar(root,orient="horizontal",length=300,mode='determinate')
progress.pack()
start_button=tk.Button(root,text="strart progress",command=start_progress)
start_button.pack(pady=10)

root.mainloop()

