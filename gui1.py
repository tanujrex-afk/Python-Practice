import tkinter as tk
window=tk.Tk()
choice=tk.StringVar(value="A")
listbox=tk.Listbox(window)
l=tk.Label(window,text="Welcome to GUI")
l.grid(row=0,column=0)
e=tk.Entry(window)
e.grid(row=0,column=1)
var=tk.IntVar()
check=tk.Checkbutton(
    window,text="Python",variable=var
)
def display():
    print("Button clicked")
button=tk.Button(
    window,text="CLick me",command=display
)
radio1=tk.Radiobutton(
    window,text="Male",variable=choice,value="Male"
)
radio2=tk.Radiobutton(
    window,text="Female",variable=choice,value="Female"
)
def show_choice():
    print(choice.get())
listbox.insert(1,"python")
listbox.insert(2,"Java")
listbox.insert(3,"ASP")
radio1.pack(side="bottom")
radio2.pack(side="right")
listbox.pack()
button.pack()
window.title("My Application")
window.geometry("400x300")
window.configure(bg="lightblue")
window.mainloop()