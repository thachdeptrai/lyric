import tkinter as tk
from tkinter import messagebox
import time
import random

def show_multiple_windows():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = 300
    window_height = 100

    def create_window():
        x = random.randint(0, screen_width - window_width)
        y = random.randint(0, screen_height - window_height)

        new_window = tk.Toplevel()
        new_window.title("Anh Nhớ Em")
        new_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        new_window.configure(bg="red")

        label = tk.Label(new_window, text="Nhớ nhớ nhớ em", font=("Arial", 12, "bold"), fg="white", bg="red")
        label.pack(expand=True)

     
    for _ in range(250):   
        root.after(100 * _, create_window)  
    root.after(20000, root.quit)

def switch_to_main_message():
    button.config(text="Anh Chỉ Muốn Nói Là", command=show_multiple_windows)

root = tk.Tk()
root.title("NgocThach Dev")
root.geometry("400x100")
root.configure(bg="pink")

button = tk.Button(root, text="Em Ơi", font=("Arial", 20), fg="black", bg="pink", command=switch_to_main_message)
button.pack(expand=True)

root.mainloop()
