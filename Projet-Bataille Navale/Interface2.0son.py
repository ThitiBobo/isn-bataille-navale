# Créé par Victorsd, le 05/05/2016 en Python 3.2
from tkinter import *
from final import*
import pygame
from pygame.locals import *
###############################################################################
#Menu Principale#
###############################################################################
class interface:
    """cette classe gère le menu principale contenant les options de son et de
    video et permet de lancer le jeu"""

    def fenprincip(self):
        """crée la fenetre principale de l'interface"""
        self.fen=Tk()
        self.fen.title("Bataille Navale")
        self.can= Canvas(self.fen, width=0, height=0)
        self.fond = PhotoImage(file="testimage2.gif")
        self.can.create_image(500, 300, image=self.fond)
        self.can.pack(padx=0, pady=0)
        self.musique()
        self.frame()
        self.menu()
        self.Menubarre()
        self.fen.mainloop()

    def frame(self):
        """définit les frames,le squelette, de l'interface"""
        #self.frame1=Frame(self.fen,bg='#682626')
        #self.frame1.pack(side=LEFT, padx=10, pady=10)

        self.frame2=Frame(self.can)
        self.frame2.pack(side=BOTTOM,padx=300,pady=100)

        self.frame3=Frame(self.can,bg='purple')
        self.frame3.pack(side=TOP,padx=0,pady=50)

    def menu(self):
        """crée les boutons permettant l'accès aux différentes fonctionnalités
        du jeu et le titre dans les frames"""

        self.b=Button(self.frame2, text ='Jouer', height=1 ,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat",command=self.play).pack(padx=0, pady=0)

        self.b1=Button(self.frame2, text ='Multijouer', height=1 ,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat").pack(padx=0,pady=0)

        self.b2=Button(self.frame2, text ='Options', height=1,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat",command=self.option).pack(padx=0,pady=0)

        self.b3=Button(self.frame2, text ='Quitter', height=1 ,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat",command=self.fin).pack(padx=0,pady=0)

        self.label=Label(self.frame3,text="Bataille Navale!",bg='purple',fg='pink',font="Elephant 80 bold",relief=RAISED).pack(side=LEFT,padx=5,pady=5)

    def fin(self):
        self.fen.destroy()
        if self.fen.destroy:
            self.sony.stop()

    def play(self):
        """détruit le canvas contenant le menu et affiche le plateau pour jouer"""
        self.can.destroy()
        test=jeu(self.fen)
        test.mainloop()
        self.can=Canvas(self.fen,width=1440,height=900,bg ='#56739A')
        self.can.pack()
        self.plat_1=plato(self.can,62,180,225,10)
###############################################################################
#OPTIONS#
###############################################################################
    def option(self):
        """détruit le canvas contenant le menu et crée de nouvelles frames ou
        sont créer de nouveaux boutons"""
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
        """créer les frames du menu option"""
        self.Frame1=Frame(self.can)
        self.Frame1.pack(side=LEFT, padx=300, pady=225)

        self.Frame2=Frame(self.Frame1)
        self.Frame2.pack(side=BOTTOM,padx=0,pady=0)

    def button(self):
        """créer les différent bouttons des options"""
        self.B1=Button(self.Frame2, text ='Son', height=1 ,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat",command=self.son).pack(padx=0, pady=0)

        self.B2=Button(self.Frame2, text ='Video', height=1,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat",command=self.video).pack(padx=0,pady=0)

        self.B3=Button(self.Frame2, text ='Menu', height=1 ,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat",command=self.remenu).pack(padx=0,pady=0)

    def remenu(self):
        """permet de revenir au menu,en détruisant la fenetre déjà existente et
        en recréant la fenetre du menu"""
        self.fen.destroy()
        self.fen=Tk()
        self.fen.title("Bataille Navale")
        self.can= Canvas(self.fen, width=0, height=0)
        self.fond = PhotoImage(file="testimage2.gif")
        self.can.create_image(500,300, image=self.fond)
        self.can.pack(padx=0, pady=0)
        self.frame()
        self.menu()
        self.Menubarre()
        self.fen.mainloop()

###############################################################################
#SON#
###############################################################################
    def son(self):
        """crée une nouvelle fenetre pour règler le son"""
        self.fen2=Tk()
        self.fen2.title("Son")
        self.can2= Canvas(self.fen2, width=0, height=0)
        #self.fond = PhotoImage(file="testimage2.gif")
        #self.can2.create_image(500,300, image=self.fond)
        self.can2.pack(padx=10, pady=10)
        self.frameson()
        self.boutons()
        self.fen2.mainloop()

    def frameson(self):
        """crée les frames de la fenetre son"""
        self.frameson=Frame(self.can2)
        self.frameson.pack(side=BOTTOM,padx=100,pady=0)

        self.frameson1=Frame(self.can2)
        self.frameson1.pack(side=TOP,padx=50,pady=50)

    def boutons(self):
        """crée les boutons pour mettre ou non du son et pour revenir sur les options"""
        self.BS=Checkbutton(self.frameson1,text="tir-canon",command=self.Music1).pack(side=LEFT,padx=10,pady=10)

        self.BS1=Checkbutton(self.frameson1,text="canon",command=self.Music2).pack(side=LEFT,padx=10,pady=10)

        self.BSR=Button(self.frameson1, text ='RETOUR', height=1,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat",command=self.fen2.destroy).pack(padx=0,pady=0)

###############################################################################
#Video#
###############################################################################
    def video(self):
         """crée une nouvelle fenetre pour règler les options video"""
         self.fen3=Tk()
         self.fen3.title("Video")
         self.can3= Canvas(self.fen3, width=300, height=225)
         #self.fond = PhotoImage(file="testimage2.gif")
         #self.can3.create_image(500,300, image=self.fond)
         self.can3.pack(padx=10, pady=10)
         self.framevideo()
         self.boutonV()
         self.fen3.mainloop()

    def framevideo(self):
        """crée les frames de la fenetre video"""
        self.framevideo=Frame(self.can3)
        self.framevideo.pack(side=BOTTOM,padx=100,pady=0)

        self.framevideo1=Frame(self.can3)
        self.framevideo1.pack(side=TOP,padx=50,pady=50)

    def boutonV(self):
        """crée les boutons pour modifier l'interface et pour revenir sur les options"""
        self.BV=Button(self.framevideo1, text ='Interface Surprise', height=1 ,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat").pack(padx=0, pady=0)

        self.BV1=Button(self.framevideo1, text ='classique', height=1,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat").pack(padx=0,pady=0)

        self.BVR=Button(self.framevideo1, text ='RETOUR', height=1,width=15, bg='#799ACC',fg='#7B6C0D',font="Elephant 30 bold",relief=GROOVE, cursor="boat",command=self.fen3.destroy).pack(padx=0,pady=0)

    def randominter(self):
        colorB=['#00FF37','#FF009E','#0077FF','#FFEF00','#6F00FF','#FF7C00']
        colorF=['#4000FF','#00F3FF','#0E721D','#7D0101','#651078','#0D6E5E']
        imagebg=[testimage2.gif]


###############################################################################
#Menubar#
###############################################################################
    def Menubarre(self):
        """crée u menubar qui permet de quitter,de revenir au menu ou de voir
        les règles du jeu depuis n'importe quelle fenetre """
        self.menubar = Menu(self.fen)
        self.menu1 = Menu(self.menubar, tearoff=0)
        self.menu1.add_command(label="Menu", command=self.remenu)
        self.menu1.add_command(label="Quitter", command=self.fen.destroy)
        self.menu1.add_separator()
        self.menubar.add_cascade(label="Menu", menu=self.menu1)
        self.fen.config(menu=self.menubar)

        self.menu2 = Menu(self.menubar, tearoff=0)
        self.menu2.add_command(label="Règles", command=self.regles)
        self.menu1.add_separator()
        self.menubar.add_cascade(label="Aide", menu=self.menu2)

    def regles(self):
        """crée une fenetre pour afficher les règles du jeu"""
        self.fen2=Tk()
        self.fen2.title("Règles")
        self.can2= Canvas(self.fen2, width=0, height=0)
        self.can2.pack(padx=0, pady=0)
        self.Labels()
        self.fen2.mainloop()

    def Labels(self):
        """crée le label contenant les règles et un bouton permettant de revenir au jeu"""
        self.label=Label(self.can2,text="1-placer vos bateaux de manière stratégique sur votre plateau\n\n2-Jouer chacun votre tour en cliquant sur une case du plateau adverse pour tirer",bg='Black',fg='White',font="Arial 20",relief=RAISED).pack(side=LEFT,padx=50,pady=50)

        self.B6=Button(self.can2, text ='Retour au jeu', height=1 ,width=10, bg='#799ACC',fg='#7B6C0D',font="Elephant 30",relief=GROOVE, cursor="boat",command=self.fen2.destroy)
        self.B6.pack(side=LEFT,padx=10,pady=10)


###############################################################################
###############################################################################

    def musique(self):
        pygame.init()
        self.sony = pygame.mixer.Sound("canon1.wav")
        self.sony.play()

    def sonmusique(self):
        self.son1 = pygame.mixer.Sound("canon1.wav")
        self.son2 = pygame.mixer.Sound("tir-canon1.wav")

    def PlaySon1(self):
        self.son1.play()

    def PlaySon2(self):
        self.son2.play()

    def Music1(self):
        if musique.get() == 1:
            self.son1.play()
        else:
            self.son1.stop()

    def Music2(self):
        if musique.get() == 1:
            self.son1.play()
        else:
            self.son1.stop()

###############################################################################
###############################################################################
class plato:
    """initialise le plateau et la taille des cases"""

    def __init__(self,can,c,x,y,nbr):
        self.c=c
        self.can=can
        self.grille(can,nbr,x,y,c)

    def grille(self,can,nbr,x,y,c):
        """crée les cases en fonction des parametres de la grille"""
        for l in range(nbr):
            can.create_rectangle(x+l*c,y,x+c+l*c,y+c,fill='blue')
            for k in range(nbr):
                can.create_rectangle(x+l*c,y+k*c,x+c+l*c,y+c+k*c,fill='#56739A')

objet = interface()
objet.fenprincip()

