import tkinter as tk
def calculate(operation):
   try:
     a=float(num1.get())
     b=float(num2.get())
     if operation=='+':
        result=a+b
     elif operation=='-':
        result=a-b
     elif operation=='*':
        result=a*b
     elif operation=='/':
        if b==0:
           answer.config(text="Error:Division by zero")
           return
        result=a/b
     answer.config(text="result="+str(result)) 
   except ValueError:
    answer.config(text="Error:Enter  valid numbers")
window=tk.Tk()
window.title("simple calcualtor")
window.geometry("300x300")
tk.Label(window,text="Enter first number").pack(pady=5)
num1 =tk.Entry(window)
num1.pack()
tk.Label(window,text="Enter the second number").pack(pady=5)
num2 =tk.Entry(window)
num2.pack()
tk.Button(window,text="Addition(+)",command=lambda: calculate("+")).pack(pady=3)
tk.Button(window,text="Subtraction(-)",command=lambda: calculate("-")).pack(pady=3)
tk.Button(window,text="Multiplication(*)",command=lambda: calculate("*")).pack(pady=3)
tk.Button(window,text="division(/)",command=lambda: calculate("/")).pack(pady=3)
answer=tk.Label(window,text="Result",font=("Arial",12,"bold"))
answer.pack(pady=10)
window.mainloop()