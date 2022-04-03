"""
main programm
"""

import tkinter as tk



root = tk.Tk()



def closeBanner(event):
    topBanner.pack_forget()

topBanner = tk.Frame(root, background="#d35c00")

topBannerLabel = tk.Label(topBanner, text="Dieses Programm befindet sich noch in Bearbeitung.", bg="#d35c00", font=("standard", 11), anchor="w")
topBannerLabel.pack(expand=1, fill="both", padx=10, pady=10, side="left")

topBannerX = tk.Label(topBanner, text="X", bg="#d35c00", font=("Fredoka", 12))
topBannerX.pack(expand=0, fill="both", padx=20, pady=10, side="right")

topBanner.pack(side="top", expand=0, fill="both")


mainContent = tk.Frame(root)
mainContent.pack(side="bottom", expand=1)

platzhalterLabel = tk.Label(mainContent, text="Platzhalter")
platzhalterLabel.pack(expand=1)



menu = tk.Menu(root, borderwidth=2)

filemenu = tk.Menu(menu, tearoff=0)
filemenu.add_cascade(label="Schließen", command=root.destroy)

modulemenu = tk.Menu(menu, tearoff=0)
modulemenu.add_cascade(label="Noch keine Module vorhanden...", state="disabled", activebackground="#f0f0f0")

menu.add_cascade(label="Datei", menu=filemenu)
menu.add_cascade(label="Module", menu=modulemenu)



topBannerX.bind("<ButtonPress-1>", closeBanner)



root.config(menu=menu)
root.title("Hescio")
root.geometry("500x350")
root.minsize(width=420, height=100)
root.mainloop()