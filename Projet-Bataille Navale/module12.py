# Créé par Victorsd, le 05/05/2016 en Python 3.2
from tkinter import*


class interface:
    def fenprincip(self):
        """crée la fenetre principale de l'interface"""
        self.fen=Tk()
        self.fen.title("Bataille Navale")
        self.frame()
        #self.menu()
        self.fen.mainloop()

    def frame(self):
        self.frame1=Frame(self.fen,bg='red').pack(side=RIGHT,padx=400,pady=400)






objet = interface()
objet.fenprincip()
