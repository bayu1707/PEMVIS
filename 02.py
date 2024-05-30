import tkinter as tk

root = tk.Tk()

Frameku = tk.Frame(root, bg = 'blue')
Frameku.place(relwidth = 0.8, relheight = 0.8)

#Latihan-4a : Membuat Button Di Root
#Tombolku = tk.Button(root, text = "Test Tombol", bg = 'gray', fg = 'red')
#Tombolku.pack()

#Latihan-4b: Membuat Button Di Frame
Tombolku = tk.Button(Frameku, text = "Tes Tombol", bg = 'gray', fg = 'red')
Tombolku.pack()

#Latihan-5 : Membuat Entry
Entryku = tk.Entry(Frameku, bg = 'green')
Entryku.pack()


root.mainloop()