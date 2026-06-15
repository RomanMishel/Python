import tkinter as tk

death_counter = 0

def death_counter():
    window = tk.Tk()

    window.title("Death Counter")

    window.geometry("400x200")

    label = tk.Label(window, text="Death Counter", font=("Arial", 20))

    label.pack(pady=20)

    def add_death(event):
        death_counter =+ 1

    def reset_death():
        death_counter = 0
    
    button = tk.Button(window, text="Reset", font=("Arial", 20), command=reset_death)

    button.pack(pady=20)

    window.bind("<+>", add_death)

    window.mainloop()

death_counter()