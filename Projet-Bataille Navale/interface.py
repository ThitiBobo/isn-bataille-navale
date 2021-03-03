# Créé par Victorsd, le 19/03/2016 en Python 3.2
from tkinter import *

class interface:
    def window(self):
        #défini
        self.fenetre=Tk()
        self.fenetre.title("Bataille Navale")
        self.frame()
        self.menu()
        self.can= Canvas(self.Frame1, width=1800, height=900, bg='blue')
        self.can.pack(padx=0, pady=0)
        self.fenetre.mainloop()

    def frame(self):
        #défini les frame de l'interface
        self.Frame1=Frame(self.fenetre,bg='red')
        self.Frame1.pack(side=LEFT, padx=0, pady=0)

        self.Frame2=Frame(self.Frame1,bg='green')
        self.Frame2.pack(side=LEFT,padx=100,pady=100)

        self.Frame3=Frame(self.Frame1,bg='pink')
        self.Frame3.pack(side=RIGHT, padx=0, pady=0)


    def menu(self):
        #défini les bouttons du menu
        self.b1=Button(self.Frame2,text='Jouer')
        self.b1.pack(padx=10,pady=10)
        self.b2=Button(self.Frame2,text='Option')
        self.b2.pack(padx=10,pady=10)
        self.b3=Button(self.Frame2,text='Quitter')
        self.b3.pack(padx=10,pady=10,command=print("test"))


objet = interface()
objet.window()