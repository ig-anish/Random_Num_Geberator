import random
import tkinter as tk
import ttkbootstrap as ttk
from customtkinter import *

def generate_number():
    result = random.randint(1, int(entry.get()))
    result_label.config(text=result)

window = tk.Tk()
window.title("Random Number Generator")
window.geometry("350x200")
style = ttk.Style(theme="cosmo")

instruction_label = ttk.Label(text="", font=("Arial", 15))
entry = CTkEntry(master=window, placeholder_text="enter the range...", width=300, text_color="white")
generate_button = ttk.Button(text="Generate", command=generate_number)
result_label = ttk.Label(text="", font=("Arial", 25))

instruction_label.pack(pady=10)
entry.place(relx=0.5, rely=0.1, anchor="center")
generate_button.pack(pady=10)
result_label.pack(pady=10)

window.mainloop()