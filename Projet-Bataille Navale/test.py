# Créé par Victorsd, le 03/03/2016 en Python 3.2
from tkinter import *
def Grille(fen,x,y):
    def onClick(event):
        click = canvas.find_closest(canvas.canvasx(event.x), canvas.canvasy(event.y))
        if canvas.itemcget(click, 'fill'):
            canvas.itemconfigure(click, fill='black')

    case=40
    canvas = Canvas(fen, width =x*case+2, height=y*case+2,)

    i = 0
    while i < x:
        j = 0
        while j < y:
            canvas.create_rectangle((i*case)+2,(j*case)+2,((i+1)*case)+2 , ((j+1)*case)+2, fill='blue')
            j+=1
        i+=1

    canvas.pack()
    canvas.bind('<ButtonRelease-1>', onClick)

fenetre=Tk()
Grille(fenetre,11,11)
fenetre.mainloop()

