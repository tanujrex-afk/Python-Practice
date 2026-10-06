import tkinter as tk
from tkinter import messagebox
import time
class MiniTimer():
    def __init__(self,root):
        self.root=root
        self.timer_id=None
        self.root.title("Fun time App")
        self.root.geometry("400x350")
        self.root.configure(bg="#2C3E50")
        self.title_label=tk.Label(root,text="Python tiume manager",font=("Arial",16,"bold"),bg="#2C3E50",fg="#ECF0F1")
        self.title_label.pack(pady=10)
        self.clock_frame=tk.LabelFrame(root,text="live Clock",bg="#2C3E50",fg="#3498DB",font=("Arial",10,"bold"))
        self.clock_frame.pack(padx=20,pady=10,fill="x")
        self.clock_label=tk.Label(
            self.clock_frame,text="",font=("Consolas",28,"bold"),bg="#2C3E50",fg="#2ECC71"
        )
        self.clock_label.pack(pady=10)
        self.timer_frame=tk.LabelFrame(root,text="countdown timer",bg="#2C3E50",fg="#3498DB",font=("Arial",10,"bold"))
        self.timer_frame.pack(padx=20,pady=10,fill="x")
        self.input_label=tk.Label(self.timer_frame,text="enter seconds:",bg="#2C3E50",fg="#ECF0F1")
        self.input_label.pack(side="left",padx=10,pady=10)
        self.entry_seconds=tk.Entry(self.timer_frame,width=10,font=("Arial",12))
        self.entry_seconds.pack(side="left",padx=10,pady=10)
        self.entry_seconds.insert(0,"10")
        self.start_btn=tk.Button(
            self.timer_frame,text="Start",command=self.start_countdown,bg="#E67E22",fg="white",font=("Arial",10,"bold"),width=8
        )
        self.start_btn.pack(side="left",padx=10,pady=10)
        self.reset_btn=tk.Button(self.timer_frame,text="Reset",command=self.stop_and_reset_timer,bg="#7F8C8D",fg="white",font=("Arial",10,"bold"),width=7)
        self.reset_btn.pack(side="left",padx=5,pady=10)
        self.countdown_label=tk.Label(
            root,text="Ready",font=("Arial",14,"italic"),bg="#2C3E50",fg="#E74C3C"
        )
        self.countdown_label.pack(pady=20)
        self.exit_btn=tk.Button(root,text="Exit to terminal",command=self.exit_application,bg="#C0392B",fg="white",font=("Arial",10,"bold"),width=15)
        self.exit_btn.pack(pady=10)
        self.update_clock()
    def update_clock(self):
        current_time=time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.root.after(1000,self.update_clock)
    def start_countdown(self):
        try:
            seconds=int(self.entry_seconds.get())
            if seconds<=0:
                raise ValueError
            self.run_countdown(seconds)
        except ValueError:
            messagebox.showerror("Invalid input","please enter a valid positive number!")
    def run_countdown(self,time_left):
        if time_left>0:
            self.countdown_label.config(text=f"Time reamining:{time_left}s",font=("Arial",14,"bold"))
            self.timer_id=self.root.after(1000,self.run_countdown,time_left-1)
        else:
            self.countdown_label.config(text="Ready")
            self.timer_id=None
            messagebox.showinfo("Times up!"," the countdown has finished!")
            self.exit_application()
    def stop_and_reset_timer(self):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id=None
        self.countdown_label.config(text="ready",font=("Arial",14,"italic"))
    def exit_application(self):
        print("\n[System] Exiting the GUI Application.....")
        self.root.quit()
        self.root.destroy()        
if __name__=="__main__":
    root=tk.Tk()
    app=MiniTimer(root)
    
    root.mainloop()