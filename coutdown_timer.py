import tkinter as tk
import time

def countdown_timer():
    
    window = tk.Tk()

    window.title("Countdown Timer")

    window.geometry("400x200")

    
    def timer():
        seconds = int(entry.get())
        label.config(text=f"User has entered: {seconds}")
        countdown(seconds)

    def countdown(seconds):
        if seconds >=0:
            label.config(text=seconds)
            window.after(1000, countdown, seconds - 1)
        else:
            label.config(text="Countdown Finished!", font=("Arial", 20))
    
    label = tk.Label(window, text="Введите секунды", font=("Arial", 20))
    label.pack(pady=20)

    entry = tk.Entry(window)
    entry.pack()

    button = tk.Button(window, text="Start", command=timer)
    button.pack(pady=15)
    
    window.mainloop()

countdown_timer()


            