"""
main programm
"""
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

platzhalterLabel = tk.Label(root, text="Platzhalter")
platzhalterLabel.pack(expand=1)

root.title("Hescio")
root.geometry("210x100")
root.mainloop()