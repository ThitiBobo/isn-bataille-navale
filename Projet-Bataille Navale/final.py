
# Créé par delplanque, le 20/04/2016 en Python 3.2
from tkinter import*
from PIL import Image, ImageTk
from random import randint as Rdom
from random import*

###############################################################################
class plateau:
    """class qui gère le plateau de chaque joueurs avec leurs bateaux,
    génèrent au début le plateau de chaque joueurs rangé dans un objet,
    les symboles de chaque bateaux sont rangés dans une liste qui représente le
    plateau du joueur, les caractéristiques de chaque bateaux sont rangés dans
    une autre liste : [ coord_x , coord_y , symbole du bateau , axe du bateau ,
    points de vies] /// la liste type sont la taille des différents bateaux
    type[0]= petit bateau, type[1]= sous-marin, type[3]= destroyer, ext ... """
    type=[2,3,3,4,5]

    def __init__(self,dim):
        """initialise le plateau"""
        self.dim=dim
        self.plat=['-']*(self.dim+2)
        for i in range(self.dim+2): self.plat[i]=['-']*(self.dim+2)
        for a in range (2):
            for b in range(self.dim+2):
                self.plat[(self.dim+1)*a][b]='+'
                self.plat[b][(self.dim+1)*a]='+'
        """initialise les bateaux"""
        self.ship=[]
        for blurp in range(5):
            self.ship.append([0,0,0,0,0])

    def check_border(self,x,y,a,axe):
        """retourne True si le bateau est placé sur un bord ou sur un bateau"""
        for blurp in range(self.type[a]):
            if self.plat[x+blurp*(axe==1)][y+blurp*(axe==0)]!='-':
                return True

    def put_ship(self,x,y,a,axe):
        """place le bateau au coordonnées sur le plateau"""
        self.ship[a]=[x,y,a,axe,self.type[a]]
        for blurp in range(self.type[a]):
            self.plat[x+blurp*(axe==1)][y+blurp*(axe==0)]=a

    def main_ship(self,x,y,a,axe):
        """place les bateaux en vérifiant la possibilité de l'emplacement"""
        if self.check_border(x,y,a,axe)!=True:
            self.put_ship(x,y,a,axe)
        else:
            return False

    def replace_ship(self,x,y,a,axe):
        """replace un bateau déja posé sur la plateau"""
        L_axe=self.ship[a][3]
        L_y=self.ship[a][1]
        L_x=self.ship[a][0]
        for blurp in range(self.type[a]):
            self.plat[L_x+blurp*(L_axe==1)][L_y+blurp*(L_axe==0)]='-'
        self.Pship(x,y,a,axe)

    def attack(self,x,y):
        """gère l'attaque des joueurs sur les bateaux, renvoie True si un
        bateau est touché sinon renvoie False si il est raté ou None si le coup
        est impossible ou déja joué"""
        if self.plat[x][y]!='+':
            if self.plat[x][y]!='°':
                if self.plat[x][y]!='*':
                    if self.plat[x][y]!='-':
                        self.ship[self.plat[x][y]][4]-=1
                        self.plat[x][y]='*'
                        return True
                    else:
                        self.plat[x][y]='°'
                        return False

    def plat_aléatoire(self,k):
        """Entrée: k=nombre de bateaux ,place des bateau de facon
        aléatoire"""
        for blurp in range(k):
            a=False
            while a==False:
                a=self.main_ship(Rdom(0,9)+1,Rdom(0,9)+1,blurp,Rdom(0,1))

    def affichage(self):
        """affiche sur la console la liste ship et plat"""
        print(self.ship)
        for a in range(self.dim+2):
            for b in range(self.dim+2):
                print(self.plat[b][a],end=" ")
            print("")

###############################################################################

class plato:

    def __init__(self,jeu,can,c,x,y,nbr,img,bto):
        self.c,self.jeu,self.can=c,jeu,can
        self.X,self.Y,self.img,self.bto=x,y,img,bto
        self.grille(can,nbr,x,y,c)
        self.blabla(nbr,x-46,y-92,c)
        self.img_bto=[]


    def grille(self,can,nbr,x,y,c):
        """Entrée: can=Canvas nbr=nombre de cases,x et y les coordonnées
        c=dimension de la case ,créer une grille de taille 'nbr' au coordonées
        'x' et 'y' avec 'c'"""
        #crée les cases en fonction des parametre de la grille
        for l in range(nbr):
            for k in range(nbr):
                self.creat_image(self.img[0],x+(c/2)+l*c,y-(c/2)+k*c)

    def blabla(self,nbr,x,y,c):
        """écrit les lettres et les chiffres autour des 2 grilles"""
        lettre='ABCDEFGHIJKLMNOPQRSTUV'
        for loop in range (nbr):
            self.can.create_text(x+c/2,y+c*loop+c*(1.5),
            text=loop+1,font=('Purisa'))
            self.can.create_text(x+c*loop+c*1.5,y+c*0.5,
            text=lettre[loop],font=('Purisa'))


    def creat_image(self,img,x,y):
        """Entrée: img=image x,y=coordonées ,foncrion qui créer une image
        au coordonnées 'x' et 'y'"""
        return self.can.create_image(x,y,image=img)

    def aléatoire(self,k,j):
        """Entrée: k=nombre de bateaux j=joueur ,fonction principale qui gère
        le placement des bateaux aléatoirement,initialise un nouveau plateau et
        y place les bateaux aléatoirement,efface les dernières images de bateaux
         et place les nouvelles aux nouvelles coordonnées"""
        j.__init__(10)
        j.plat_aléatoire(k)
        self.del_img()
        self.aff_aléatoire(k,j)

    def aff_aléatoire(self,k,j):
        """ Entrée: k=nombre de bateaux j=joueur , affiche les bateaux et les
        ranges dans la liste'self.img_bto'"""
        for blurp in range(k):
            x,y=j.ship[blurp][0]*46+self.X-23,j.ship[blurp][1]*46+self.Y-69
            axe=j.ship[blurp][3]
            if axe==0:
                k1,k2=0,23*(j.type[blurp]-1)
            else:
                k1,k2=23*(j.type[blurp]-1),0
            self.img_bto.append(self.creat_image(self.bto[axe+choice([0,
            2])][blurp],x+k1,y+k2))

    def del_img(self):
        """efface l'image des bateaux dans la liste 'self.img_bto' et recréer
        une nouvelle liste"""
        for blurp in range(len(self.img_bto)):
            self.can.delete(self.img_bto[blurp])
        self.img_bto=[]




###############################################################################
class game_menu:

    def __init__(self,jeu):
        self.jeu=jeu
        self.can=self.jeu.can
        self.game_barre()
        self.button()
        self.can.bind("<Button-1>",self.clic)


    def game_barre(self):
        self.can.create_rectangle(0,700,1440,900,fill='red',
                outline='red')


    def button(self):
        self.but=[]
        self.but.append(self.can.create_rectangle(840,737,950,783,fill='green',
                outline='red'))
        self.but.append(self.can.create_rectangle(490,737,600,783,fill='green',
                outline='red'))
        self.but.append(self.can.create_rectangle(620,730,820,790,fill='green',
                outline='red'))

    def clic(self,event):
        X,Y=event.x,event.y
        [xmin,ymin,xmax,ymax] = self.can.coords(self.but[0])
        if  xmin<=X<=xmax and ymin<=Y<=ymax:
            self.jeu.plat_2.aléatoire(5,self.jeu.j2)

        [xmin,ymin,xmax,ymax] = self.can.coords(self.but[1])
        if  xmin<=X<=xmax and ymin<=Y<=ymax:
            self.jeu.plat_1.aléatoire(5,self.jeu.j1)

        [xmin,ymin,xmax,ymax] = self.can.coords(self.but[2])
        if  xmin<=X<=xmax and ymin<=Y<=ymax:
            self.partie=partie(self.can,[self.jeu.j1,158,169,46,10],[self.jeu.j2,822,169,46,10])
            self.can.bind("<Button-1>",self.partie.attaque)


###############################################################################
class mouvement:
    def __init__(self,can,img):
        self.can=can
        self.vrai=False
        self.img=img
        self.can.bind("<Button-1>",self.clic)
        self.can.bind("<Button1-Motion>",self.reste)

    def creat_image(self,img,x,y):
            return self.can.create_image(x,y,image=img)

    def clic(self,event):
        self.x1,self.y1=event.x,event.y
        self.selObject=self.can.find_closest(self.x1, self.y1)

    def reste(self,event):
            self.x2,self.y2=event.x,event.y
            self.dx, self.dy = self.x2-self.x1, self.y2-self.y1
            self.can.move(self.selObject,self.dx,self.dy)
            self.x1, self.y1 = self.x2, self.y2

###############################################################################
class partie:

    def __init__(self,can,j1,j2):
        self.can=can
        self.j1=j1
        self.j2=j2#[j2,x,y,c,nbr]
        self.T=1

    def attaque(self,event):
        x,y=event.x,event.y
        V=None
        if self.T==1: j,a=self.j2,2
        else: j,a=self.j1,1

        if j[1]<x<j[1]+j[3]*(j[4]) and j[2]-46<y<j[2]+j[3]*(j[4]) :
            print("ok")
            V=j[0].attack((x-j[1])//j[3]+1,(y-j[2])//j[3]+2)
            x,y=(x-j[1])//j[3]*j[3]+j[1]+23,(y-j[2])//j[3]*j[3]+j[2]+23
            if V==True:
                self.can.create_oval(x-10, y-10, x+10, y+10, outline='black', fill='red')
                self.T=a
            if V==False:
                self.can.create_oval(x-10, y-10, x+10, y+10, outline='blue', fill='blue')
                self.T=a
            if V==None:
                print("nul!")
        j[0].affichage()

###############################################################################
###############################################################################
class jeu:

    def __init__(self,root):
        self.root=root
        self.option()
        self.claim_objet()
        self.j1.affichage()

    def claim_objet(self):
        self.menu=game_menu(self)
        self.init_player()

    def init_player(self):
        self.j1=plateau(10)
        self.j2=plateau(10)
        self.plat_1=plato(self,self.can,46,158,169,10,self.img_terrain,self.img_bto)
        self.plat_2=plato(self,self.can,46,822,169,10,self.img_terrain,self.img_bto)
        #ev=mouvement(self.can,self.img_bto)

    def option(self):
        self.can=Canvas(self.root,width=1440,height=900,bg ='#56739A')
        self.can.pack()
        self.img_bto=self.init_image()
        self.img_terrain=self.list_piece(('img/terrain_1.png','img/terrain_1.png'))

    def list_piece(self,I):
        """importation des images des pièces de jeu"""
        img=[]
        for blurp in range(len(I)):
            img.append(ImageTk.PhotoImage(Image.open(I[blurp])))
        return img

    def init_image(self):
        img1=self.list_piece(('img/destroyer1.png','img/croiseur1.png','img/sous-marin1.png','img/cuirassé1.png','img/porte_avions1.png'))
        img2=self.list_piece(('img/destroyer2.png','img/croiseur2.png','img/sous-marin2.png','img/cuirassé2.png','img/porte_avions2.png'))
        img3=self.list_piece(('img/destroyer3.png','img/croiseur3.png','img/sous-marin3.png','img/cuirassé3.png','img/porte_avions3.png'))
        img4=self.list_piece(('img/destroyer4.png','img/croiseur4.png','img/sous-marin4.png','img/cuirassé4.png','img/porte_avions4.png'))
        return [img1,img2,img3,img4]

    def mainloop(self):
        self.root.mainloop()

###############################################################################
###############################################################################
