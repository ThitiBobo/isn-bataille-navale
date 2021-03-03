# Créé par savary-derelle, le 01/03/2016 en Python 3.2
from math import*
from tkinter import*

def plat():
    canvas.create_text(500, 200, text="Bataille Navale", font="Arial 80 italic", fill="blue")
    canvas.create_text(500, 300, text="Jouer", font="Arial 40 italic", fill="black")
    canvas.create_text(500, 400, text="options", font="Arial 40 italic", fill="black")



fenetre = Tk()
canvas = Canvas(fenetre, width=1000, height=800, background='white')
bidule()
canvas.pack()
fenetre.mainloop()
