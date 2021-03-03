# Créé par Steph, le 08/02/2016 en Python 3.2

from tkinter import *
#-------------------------------------------------------------------------------
def Grille(fen,x,y):
    def onClick(event):

        if canvas.itemcget(monitem, 'fill') == 'white':
            canvas.itemconfigure(monitem, fill='black')
        else:
            canvas.itemconfigure(monitem, fill='white')

    "Dessine la grille"
    taille_case=60
    canvas = Canvas(fen, width =x*taille_case+4, height=y*taille_case+4)

    i = 0
    while i < x:
        j = 0
        while j < y:
            canvas.create_rectangle((i*taille_case)+2,(j*taille_case)+2,((i+1)*taille_case)+2 , ((j+1)*taille_case)+2, fill='white')
            j+=1
        i+=1

    canvas.pack()
    canvas.bind('<ButtonRelease-1>', onClick)
#-------------------------------------------------------------------------------
def Apercu(fen,x,y):
    "Dessine l'aperçu"
    taille_case=5
    canvas = Canvas(fen, width =x*taille_case+4, height=y*taille_case+4)

    i = 0
    while i < x:
        j = 0
        while j < y:
            canvas.create_rectangle((i*taille_case)+2,(j*taille_case)+2,((i+1)*taille_case)+2 , ((j+1)*taille_case)+2, outline='white',fill='white')
            j+=1
        i+=1

    canvas.pack()
#-------------------------------------------------------------------------------
root = Tk()
Apercu(root,25,25)
Grille(root,25,25)
root.mainloop()