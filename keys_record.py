import tkinter as tk

def key_record(event):
    label.config(text=event.keysym)

window = tk.Tk()

window.title("Key Recorder")

window.geometry("400x200")

window.bind("<Key>", key_record)

label = tk.Label(window, font=("Arial",50))

label.pack()

window.mainloop()

key_record()