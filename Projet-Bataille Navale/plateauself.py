# Créé par savary-derelle, le 04/03/2016 en Python 3.2
from tkinter import *

class platotest:

    def fourretout(self,can,nbr,x,y,c):
        """fonction prncipale qui paramètre le plateau"""
        self.can=can
        self.grille(10,50,50,50)
        self.can.bind('<ButtonRelease-1>', self.souris)


    def blabla(self,nbr,x,y,c):
        """écrit les lettres et les chiffres autour des 2 grilles"""
        lettre='ABCDEFGHIJK'
        for loop in range (nbr):
            self.can.create_text(x+c/2,y+c*loop+c*(1.5),text=loop+1,font=('Purisa'))
            self.can.create_text(x+c*loop+c*1.5,y+c*0.5,text=lettre[loop],font=('Purisa'))

    def grille(self,nbr,x,y,c):
        """crée les cases en fonction des parametre de la grille"""
        for l in range(nbr):
            self.can.create_rectangle(x+l*c,y,x+c+l*c,y+c)
            for k in range(nbr):
                self.can.create_rectangle(x+l*c,y+k*c,x+c+l*c,y+c+k*c)
        self.blabla(nbr,x-c,y-c,c)

    def souris(self,event):
            click = self.can.find_closest(self.can.canvasx(event.x), self.can.canvasy(event.y))
            if self.can.itemcget(click, 'fill'):
                self.can.itemconfigure(click, fill='green')
root=Tk()
can = Canvas(root, width =8000, height=8000)
can.pack()
objet = platotest()
objet.fourretout(can,10,50,50,70)
root.mainloop()