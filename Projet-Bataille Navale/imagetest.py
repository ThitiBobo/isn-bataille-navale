# Créé par Victorsd, le 11/05/2016 en Python 3.2
from tkinter import *
root = Tk()
c = Canvas(root,)
c.pack()
fond = PhotoImage(file="ocean.gif")
c.create_image(0, 0, image=fond)
root.mainloop()
