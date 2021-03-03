# Créé par Victorsd, le 05/05/2016 en Python 3.2
from tkinter import *
from final import*
###############################################################################
#Menu Principale#
###############################################################################
class interface:
    def fenprincip(self):
        """crée la fenetre principale de l'interface"""
        self.fen=Tk()
        self.fen.title("Bataille Navale")
        self.can= Canvas(self.fen, width=0, height=0)
        self.fond = PhotoImage(file="testimage2.gif")
        self.can.create_image(500, 300, image=self.fond)
        self.can.pack(padx=0, pady=0)
        self.frame()
        self.menu()
        self.Menubarre()
        self.fen.mainloop()

    def frame(self):
        """définit les frames de l'interface"""
        #self.frame1=Frame(self.fen,bg='#682626')
        #self.frame1.pack(side=LEFT, padx=10, pady=10)

        self.frame2=Frame(self.can)
        self.frame2.pack(side=BOTTOM,padx=300,pady=100)

        self.frame3=Frame(self.can)
        self.frame3.pack(side=TOP,padx=0,pady=50)

    def menu(self):
        """crée les boutons et le titre dans les frames"""

        self.b1=Button(self.frame2, text ='Jouer', height=1 ,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat",command=self.play).pack(padx=0, pady=0)

        self.b2=Button(self.frame2, text ='Multijoueurs', height=1,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat").pack(padx=0,pady=0)

        self.b3=Button(self.frame2, text ='Options', height=1 ,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat",command=self.option).pack(padx=0,pady=0)

        self.b4=Button(self.frame2, text ='Quitter', height=1 ,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat",command=self.fen.destroy).pack(padx=0,pady=0)

        self.label=Label(self.frame3,text="Bataille Navale!",bg='purple',fg='pink',font="Elephant 80 bold",relief=RAISED).pack(side=LEFT,padx=0,pady=0)

    def play(self):
        """détruit le menu et affiche le plateau pour jouer"""
        self.can.destroy()
        test=jeu(self.fen)
        test.mainloop()
        self.can=Canvas(self.fen,width=1440,height=900,bg ='#56739A')
        self.fond = PhotoImage(file="testimage2.gif")
        self.can.create_image(500, 300, image=self.fond)
        self.can.pack()
        self.plat_1=plato(self.can,62,180,225,10)
###############################################################################
#OPTIONS#
###############################################################################
    def option(self):
        """détruit le canvas et crée des nouvelles frames"""
        self.can.destroy()
        self.can= Canvas(self.fen, width=0, height=0)
        self.fond = PhotoImage(file="testimage2.gif")
        self.can.create_image(500, 300, image=self.fond)
        self.can.pack(padx=0, pady=0)
        self.frames()
        self.button()
        self.Menubarre()
        self.fen.mainloop()

    def frames(self):
        #self.Frame1=Frame(self.can,bg='#682626')
        #self.Frame1.pack(side=LEFT, padx=10, pady=10)

        self.Frame2=Frame(self.can,bg='#516139')
        self.Frame2.pack(side=BOTTOM,padx=200,pady=100)

    def button(self):
        """créer les différent bouttons des options"""
        self.B1=Button(self.Frame2, text ='Son', height=1 ,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat",command=self.fen.destroy).pack(padx=0, pady=0)

        self.B2=Button(self.Frame2, text ='Video', height=1,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat").pack(padx=0,pady=0)

        self.B3=Button(self.Frame2, text ='Menu', height=1 ,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat",command=self.remenu).pack(padx=0,pady=0)

        self.B4=Button(self.Frame2, text ='Quitter', height=1 ,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat",command=self.fen.destroy).pack(padx=0,pady=0)

    def remenu(self):
        """permet de revenir au menu pour lancer une partie"""
        self.can.destroy()
        self.can= Canvas(self.fen, width=0, height=0)
        self.fond = PhotoImage(file="testimage2.gif")
        self.can.create_image(500, 300, image=self.fond)
        self.can.pack(padx=0, pady=0)
        self.frame()
        self.menu()
        self.Menubarre()
###############################################################################
#Menubar#
###############################################################################
    def Menubarre(self):
        self.menubar = Menu(self.fen)
        self.menu1 = Menu(self.menubar, tearoff=0)
        self.menu1.add_command(label="Menu", command=self.fenprincip)
        self.menu1.add_command(label="Quitter", command=self.fen.destroy)
        self.menu1.add_separator()
        self.menubar.add_cascade(label="Menu", menu=self.menu1)
        self.fen.config(menu=self.menubar)

        self.menu2 = Menu(self.menubar, tearoff=0)
        self.menu2.add_command(label="Règles", command=self.regles)
        self.menu1.add_separator()
        self.menubar.add_cascade(label="Aide", menu=self.menu2)

    def regles(self):
        self.fen2=Tk()
        self.fen2.title("Règles")
        self.can2= Canvas(self.fen2, width=0, height=0, bg='blue')
        self.can2.pack(padx=0, pady=0)
        self.Labels()
        self.fen2.mainloop()

    def Labels(self):
        self.label=Label(self.can2,text="Bataille Navale!",bg='Black',fg='White',font="Arial 20",relief=RAISED).pack(side=LEFT,padx=50,pady=50)

        self.B6=Button(self.can2, text ='Retour au jeu', height=1 ,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30",relief=GROOVE, cursor="boat",command=self.fen2.destroy).pack(padx=20,pady=20)

###############################################################################
    def imagefond(self):
        root = Tk()
        self.can = Canvas(root,)
        c.pack()
        fond = PhotoImage(file="ocean.gif")
        c.create_image(0, 0, image=fond)
        root.mainloop()

###############################################################################
class plato:

    def __init__(self,can,c,x,y,nbr):
        self.c=c
        self.can=can
        self.grille(can,nbr,x,y,c)

    def grille(self,can,nbr,x,y,c):
        #crée les cases en fonction des parametre de la grille
        for l in range(nbr):
            can.create_rectangle(x+l*c,y,x+c+l*c,y+c,fill='blue')
            for k in range(nbr):
                can.create_rectangle(x+l*c,y+k*c,x+c+l*c,y+c+k*c,fill='#56739A')

objet = interface()
objet.fenprincip()