import tkinter as tk
import time

def countdown():
    
    window = tk.Tk()

    window.title("Countdown Timer")

    window.geometry("400x200")

    def timer():
        seconds = entry.get()
        print(f"User has entered: {seconds}")

        while seconds > 0:
            minutes = seconds // 60
            remaining_time = seconds % 60
            time.sleep(1)
            seconds -= 1
        label = tk.Label(window, text=f"{minutes:02}:{remaining_time:02}", font=("Arial", 20))

        label.pack(pady=20)

        entry = tk.Entry(window)


            