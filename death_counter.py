import tkinter as tk
import keyboard as kb

def death_counter():
    window = tk.Tk()

    window.title("Death Counter")

    window.geometry("400x200")

    label = tk.Label(window, text="Death Counter", font=("Arial", 20))

    death_counter = int(0)

    user_input = bind(".")

    def add_death():
        if user_input() == True:
            death_counter += 1
            label.config(text=f"Deaths count: {death_counter}")

    def reset_death():
        if user_input.get() == "Reset":
            death_counter = 0

    button = tk.Button(window, text="+", font=("Arial", 20), command=add_death)

    button.pack(pady=20)

    button = tk.Button(window, text="Reset", font=("Arial", 20), command=reset_death)

    button.pack(pady=20)

    window.mainloop()

death_counter()