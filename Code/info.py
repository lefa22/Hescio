import tkinter as tk

icon = 0

def show():
    infoFenster = tk.Tk()

    infoFenster.title("Info")
    infoFenster.geometry(f"400x200+{int(infoFenster.winfo_screenwidth()/2-400/2)}+{int(infoFenster.winfo_screenheight()/2-200/2)}")
    infoFenster.resizable(width=0, height=0)
    infoFenster.mainloop()

#show()