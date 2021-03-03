
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
        """initialise un plateau en fonction de x,y,c,nbr et affiche les images
        de la liste img"""
        self.c,self.jeu,self.can=c,jeu,can
        self.X,self.Y,self.img,self.bto=x,y,img,bto
        self.grille(can,nbr,x,y,c)
        self.blabla(nbr,x-46,y-92,c)

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
            text=loop+1,font=('Purisa'),fill='white')
            self.can.create_text(x+c*loop+c*1.5,y+c*0.5,
            text=lettre[loop],font=('Purisa'),fill='white')

    def creat_image(self,img,x,y):
        """Entrée: img=image x,y=coordonées ,foncrion qui créer une image
        au coordonnées 'x' et 'y'"""
        return self.can.create_image(x,y,image=img)

###############################################################################
class game_menu:

    def __init__(self,jeu):
        """initialise l'interface menu du jeu avec ses bouttons"""
        self.button=[]
        self.jeu=jeu
        self.img=jeu.img_terrain
        self.can=self.jeu.can
        self.partie_start=False
        self.init_button()
        self.creat_image(self.img[2],550,734)
        self.barre_pseudo(296,69,'joueur 1')
        self.barre_pseudo(822,69,'ordinateur')
        self.boutton(self.img[3],147,697)
        self.boutton(self.img[5],147,769)
        self.can.bind("<Button-1>",self.clic)
        self.can.bind("<Button1-Motion>",self.jeu.mouv.reste)
        self.can.bind('<ButtonRelease-1>',self.button_release)
        self.jeu.root.bind("<MouseWheel>",self.jeu.mouv.suite)

    def init_button(self):
        """créer deux rectangle pour les bouttons"""
        self.but=[]
        self.but.append(self.can.create_rectangle(66,674,227,720,fill='',
                outline='red'))

        self.but.append(self.can.create_rectangle(66,746,227,792,fill='green',
                outline='red'))

    def barre_pseudo(self,x,y,name):
        """créer une barre pour afficher le nom des joueurs"""
        self.creat_image(self.img[1],x,y)
        self.can.create_text(x,y,text=name,font=('Purisa'),fill='white')

    def boutton(self,img1,x,y):
        """place l'image du boutton"""
        self.button.append(self.creat_image(img1,x,y))

    def boutton_press(self,a,img):
        """permet l'animation des bouttons"""
        x,y=self.can.coords(self.button[a])
        self.can.delete(self.button[a])
        self.button[a]=self.creat_image(img,x,y)

    def button_release(self,event):
        self.boutton_press(0,self.img[3])
        self.boutton_press(1,self.img[5])
        if self.partie_start==False:
            self.jeu.mouv.clic(event)
            if self.jeu.mouv.vrai==True:
                self.jeu.mouv.vrai=False
                self.jeu.mouv.placement(event)

    def creat_image(self,img,x,y):
        """Entrée: img=image x,y=coordonées ,foncrion qui créer une image
        au coordonnées 'x' et 'y'"""
        return self.can.create_image(x,y,image=img)

    def clic(self,event):
        """détecte quelle boutton a était préssé"""
        X,Y=event.x,event.y
        [xmin,ymin,xmax,ymax] = self.can.coords(self.but[0])
        if  xmin<=X<=xmax and ymin<=Y<=ymax:
            self.boutton_press(0,self.img[4])
            self.jeu.mouv.aléatoire(5,self.jeu.j1)
        [xmin,ymin,xmax,ymax] = self.can.coords(self.but[1])
        if  xmin<=X<=xmax and ymin<=Y<=ymax:
            self.boutton_press(1,self.img[6])
            self.partie=partie(self.can,[self.jeu.j1,66,188,46,10],[self.jeu.j2,592,188,46,10],self.img)
            self.can.bind("<Button-1>",self.partie.attaque)
            self.partie_start=True
        self.jeu.mouv.clic(event)

###############################################################################
class mouvement:
    def __init__(self,game):
        """initialise la classe mouvement"""
        self.game=game
        self.can=game.can
        self.vrai=False
        self.select=-1
        self.img=game.img_bto
        self.bateau()
        self.ima()
        self.aléatoire(5,self.game.j1)

    def create_image(self,img,x,y):
        """créer une image au coordonnée x et y"""
        return self.can.create_image(x,y,image=img)

    def list_piece(self,I):
        """importation des images des pièces de jeu"""
        img=[]
        for blurp in range(len(I)):
                img.append(ImageTk.PhotoImage(Image.open(I[blurp])))
        return img

    def ima(self):
        """créer une liste pour leur orientation,affiche tout les bateaux,
        replace les images sur leur hitbox"""
        self.image_bateau=[]
        self.orientation=[1,1,1,1,1]
        self.image_bateau.append(self.create_image(self.img[1][0],0,0))
        self.image_bateau.append(self.create_image(self.img[1][1],0,0))
        self.image_bateau.append(self.create_image(self.img[1][2],0,0))
        self.image_bateau.append(self.create_image(self.img[1][3],0,0))
        self.image_bateau.append(self.create_image(self.img[1][4],0,0))
        for loop in range(5):
            self.affichage(loop)

    def orient(self,Y):
        """permet de tourner l'image d'un bateau"""
        self.orientation[Y]+=1
        if self.orientation[Y]>3:
            self.orientation[Y]=0
        if self.orientation[Y]<0:
            self.orientation[Y]=3
        self.can.delete(self.image_bateau[Y])
        self.image_bateau[Y]=self.create_image(self.img[self.orientation[Y]][Y],0,0)
        self.affichage(Y)

    def affichage(self,X):
        """affiche l'image sur sa hitbox"""
        [xmin,ymin,xmax,ymax]=self.can.coords(self.hitbox[X])
        x,y=(xmin+xmax)/2,(ymin+ymax)/2
        self.can.coords(self.image_bateau[X],x,y)

    def carre(self,t,x,y):
        """ réinitialise les paramètres du bateau """
        return self.can.create_rectangle(x,y,x+t*46,y+46,outline="")

    def bateau(self):
            """ créer 5 bateaux et détermine les paramètres """
            t=[2,3,3,4,5]
            self.hitbox=[]
            for loop in range(5):
                self.hitbox.append(self.carre(t[loop],200,200+loop*56))

    def clic(self,event):
        """ créer l'évenement clic et détermine les coordonnées de l'objet """
        self.vrai=False
        x1,y1=event.x,event.y
        for loop in range (len(self.hitbox)):
            x3,y3,x4,y4=self.can.coords(self.hitbox[loop])
            if x3<x1<x4 and y3<y1<y4:
                self.vrai=True
                self.select=loop
                break
            else:self.vrai=False

    def reste(self,event):
        """ si les coordonées de l'objet sont exacte alors déplace les carrés """
        if self.vrai==True :
            x,y=event.x,event.y
            [xmin,ymin,xmax,ymax] = self.can.coords(self.hitbox[self.select])
            mx,my=(xmax-xmin)/2,(ymax-ymin)/2
            x,y=self.aligne_grille(x,y,self.select)
            self.can.coords(self.hitbox[self.select],x-mx,y-my,x+mx,y+my)
            self.affichage(self.select)

    def suite(self,event):
        """ création de l'evenement molette - horizontal ou vertical """
        if self.vrai==True :
            x,y=event.x,event.y
            [xmin,ymin,xmax,ymax] = self.can.coords(self.hitbox[self.select])
            tx,ty=xmax-xmin,ymax-ymin
            mx,my=(xmax+xmin)/2,(ymax+ymin)/2
            self.can.coords((self.hitbox[self.select]),mx-ty/2,my-tx/2,mx+ty/2,my+tx/2)
            self.orient(self.select)
            self.reste(event)

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
            x,y=j.ship[blurp][0]*46+66-23,j.ship[blurp][1]*46+188-69
            axe=j.ship[blurp][3]
            if axe==0:
                k1,k2=0,23*(j.type[blurp]-1)
            else:
                k1,k2=23*(j.type[blurp]-1),0
            ax=axe+choice([0,2])
            self.orientation[blurp]=ax
            self.image_bateau.append(self.creat_image(self.img[ax][blurp],x+k1,
            y+k2))
            self.hitbox_alea(x+k1,y+k2,axe,blurp)

    def hitbox_alea(self,x,y,axe,n):
        """replace les hitbox suite à un placement aléatoire"""
        t=[2,3,3,4,5]
        [xmin,ymin,xmax,ymax]=self.can.coords(self.hitbox[n])
        if axe==0:
            a,b=1,t[n]
        else:
            b,a=1,t[n]
        self.can.coords(self.hitbox[n],x-(a*46)/2,y-(b*46)/2,x+(a*46)/2,
        y+(b*46)/2)

    def aligne_grille(self,x,y,t):
        """aligne les hitbox sur la grille du joueur"""
        [xmin,ymin,xmax,ymax] = self.can.coords(self.hitbox[t])
        tx,ty=xmax-xmin,ymax-ymin
        a,b=23,23
        if tx==92 or ty==92 or tx==184 or ty==184:
            if tx==92 or tx==184:a,b=0,23
            if ty==92 or ty==184:a,b=23,0
        if 142<y<602 and 66<x<528:
            x=(x-66)//46*46+66+a
            y=(y-142)//46*46+142+b
        return x,y

    def placement(self,event):
        """place les bateaux sur la grille"""
        x,y,ship=event.x,event.y,False
        [xmin,ymin,xmax,ymax] = self.can.coords(self.hitbox[self.select])
        k=2
        if self.select==1 or self.select==2 or self.select==0:k=1
        axe,a,b=1,0*k,-1*k
        if xmax-xmin == 46:axe,a,b=0*k,-1*k,0
        x,y=(x-20)//46,(y-96)//46
        if self.select!=-1:
            ship=self.game.j1.replace_ship(x+b,y+a,self.select,axe)
            if 0<=x<=11 and 0<=y<=11:
                self.game.j1.main_ship(x+b,y+a,self.select,axe)
            self.game.j1.affichage()

    def del_img(self):
        """efface l'image des bateaux dans la liste 'self.img_bto' et recréer
        une nouvelle liste"""
        for blurp in range(len(self.image_bateau)):
            self.can.delete(self.image_bateau[blurp])
        self.image_bateau=[]

###############################################################################
class partie:

    def __init__(self,can,j1,j2,img):
        self.ia=ia_facile(j1[0])
        j2[0].plat_aléatoire(5)
        self.img=img
        self.can=can
        self.j1=j1
        self.j2=j2#[j2,x,y,c,nbr]
        self.T=1

    def attaque(self,event):
        x,y=event.x,event.y
        j,a=self.j2,2
        if j[1]<x<j[1]+j[3]*(j[4]) and j[2]-46<y<j[2]+j[3]*(j[4]) :
            V=j[0].attack((x-j[1])//j[3]+1,(y-j[2])//j[3]+2)
            x,y=(x-j[1])//j[3]*j[3]+j[1]+23,(y-j[2])//j[3]*j[3]+j[2]+23
            if V==True:
                self.creat_image(self.img[8],x,y)
                self.A_ia()
            if V==False:
                self.creat_image(self.img[7],x,y)
                self.A_ia()
            self.fin_partie(self.j2[0].ship)

    def A_ia(self):
        V,x,y=self.ia.IA_attack()
        x,y=x*46+66+23,y*46+188-69
        if V==None:
                self.creat_image(self.img[8],x,y)
        if V==False:
                self.creat_image(self.img[7],x,y)
        self.fin_partie(self.j1[0].ship)


    def fin_partie(self,j):
        if j[0][4]==0 and j[1][4]==0 and j[2][4]==0 and j[3][4]==0 and j[4][4]==0:
            print("fin de partie")
            self.creat_image(self.img[9],549,409)

    def creat_image(self,img,x,y):
        """Entrée: img=image x,y=coordonées ,foncrion qui créer une image
        au coordonnées 'x' et 'y'"""
        return self.can.create_image(x,y,image=img)

###############################################################################
class ia_facile:

    def __init__(self,plateau):
        self.plateau1=plateau
        self.l=self.list_l()

    def IA_attack(self):
        k=None
        while k == None:
            a=choice(self.l)
            y=(a//10)+1
            x=a-10*(y-1)
            k=self.plateau1.attack(x+1,y)
        self.l=self.delet(self.l,a)
        while k==True:
            k=self.plateau1.attack(x+1,y)
            if k==False:
                    k=self.plateau1.attack(x,y+1)
                    while k==True:
                        k=self.plateau1.attack(x,y+1)
                        if k==False:
                            k=self.plateau1.attack(x-1,y)
                            while k==True:
                                k=self.plateau1.attack(x-1,y)
                                if k==False:
                                    k=self.plateau1.attack(x,y-1)
                                    while k==True:
                                        k=self.plateau1.attack(x,y-1)
        return k,x,y


    def list_l(self):
        l=[]
        for loop in range(100):
            l.append(loop+1)
        return l

    def delet(self,li,a):
        """"met dans une nouvelle liste tout les élèments d'une liste donnée
        sauf celui voulut, retourne la nouvelle liste """
        l=[]
        for loop in range(len(li)):
            if li[loop]!=a:
                l.append(li[loop])
        return l


###############################################################################
###############################################################################
class jeu:

    def __init__(self,root):
        self.root=root
        self.option()
        self.claim_objet()

    def claim_objet(self):
        self.init_player()
        self.mouv=mouvement(self)
        self.menu=game_menu(self)


    def init_player(self):
        self.j1=plateau(10)
        self.j2=plateau(10)
        self.plat_1=plato(self,self.can,46,66,188,10,self.img_terrain,self.img_bto)
        self.plat_2=plato(self,self.can,46,592,188,10,self.img_terrain,self.img_bto)

    def option(self):
        self.can=Canvas(self.root,width=1098,height=818,bg ='#56739A')
        self.can.pack()
        self.img_bto=self.init_image()
        self.img_terrain=self.list_piece(('img/terrain_1.png',
        'img/terrain_3.png','img/terrain_4.png','img/balea_1.png',
        'img/balea_2.png','img/bjouer_1.png','img/bjouer_2.png',
        'img/tire_1.png','img/tire_2.png','img/FIN.png'))

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



