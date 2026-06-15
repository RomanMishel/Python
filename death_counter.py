import tkinter as tk

death_counter = 0

def death_count():
    window = tk.Tk()

    window.title("Death Counter")

    window.geometry("400x200")

    def add_death(event):
        global death_counter
        death_counter += 1
        label.config(text=f"Death Counter: {death_counter}")
        
    def reset_death():
       global death_counter
       death_counter = 0
       label.config(text=f"Death Counter: {death_counter}")
    
    label = tk.Label(window, text=f"Death Counter: {death_counter}", font=("Arial", 20))

    label.pack(pady=20)

    button = tk.Button(window, text="Reset", font=("Arial", 20), command=reset_death)

    button.pack(pady=20)

    window.bind("<+>", add_death)

    window.mainloop()

death_count()