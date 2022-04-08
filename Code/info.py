def show():
    import tkinter as tk

    root = tk.Tk()

    root.title("Info")
    root.geometry(f"400x200+{int(root.winfo_screenwidth()/2-400/2)}+{int(root.winfo_screenheight()/2-200/2)}")
    root.resizable(width=0, height=0)
    root.mainloop()