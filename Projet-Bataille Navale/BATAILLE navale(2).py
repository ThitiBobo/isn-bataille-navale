# Créé par crepin, le 20/04/2016 en Python 3.2
### importation des bibliothèques ###
from tkinter import*
from PIL import Image, ImageTk
### fin ###

### début classe déplacement bateau ###
class mouvement:
    ### debut fonction de la classe ###
    def __init__(self,can,x,y):
        """ initialise les paramètre """
        self.can=can
        self.vrai=False
        self.img=self.image()
        self.apparait()
        self.bateau()

    def carre(self,t,x,y):
        """ réinitialise les paramètres du bateau """
        return self.can.create_rectangle(x,y,x+t*46,y+46,outline="white")

    def bateau(self):
        """ créer 5 bateaux et détermine les paramètres """
        t=[2,3,3,4,5]
        self.hitbox=[]
        for loop in range(5):
            self.hitbox.append(self.carre(t[loop],2,2+loop*56))

    def clic(self,event):
        """ créer l'évenement clic et détermine les coordonnées de l'objet """
        self.vrai=False
        x1,y1=event.x,event.y
        for loop in range (len(self.hitbox)):
            x3,y3,x4,y4=self.can.coords(self.hitbox[loop])
            if x3<x1<x4 and y3<y1<y4:
                self.vrai=True
                self.select=loop

    def reste(self,event):
        """ si les coordonées de l'objet sont exacte alors déplace les carrés """
        if self.vrai==True :
            x,y=event.x,event.y
            [xmin,ymin,xmax,ymax] = self.can.coords(self.hitbox[self.select])
            mx,my=(xmax-xmin)/2,(ymax-ymin)/2
            self.can.coords(self.hitbox[self.select],x-mx,y-my,x+mx,y+my)
            c=self.limite(x,y)

    def suite(self,event):
        """ création de l'evenement molette - horizontal ou vertical """
        [xmin,ymin,xmax,ymax] = self.can.coords(self.hitbox[self.select])
        tx,ty=xmax-xmin,ymax-ymin
        mx,my=(xmax+xmin)/2,(ymax+ymin)/2
        self.can.coords((self.hitbox[self.select]),my-ty/2,mx-tx/2,my+ty/2,mx+tx/2)

    def limite(self,x,y):
        """ evite de sortir l'objet du canevas """
        c=[x,y]
        if x<0:
            c[0]=0
        if x>500-20:
            c[0]=500-20
        if y<0:
            c[1]=0
        if y>300-20:
            c[1]=300-20
        return c

    def list_piece(self,I):
        """ importation des images """
        img=[]
        for blurp in range(len(I)):
            img.append(ImageTk.PhotoImage(Image.open(I[blurp])))
        return img

    def image(self):
        """ importe les bateaux, ranger dans une liste """
        img1=self.list_piece(('img/destroyer1.png','img/croiseur1.png','img/sous-marin1.png','img/cuirassé1.png','img/porte_avions1.png'))
        img2=self.list_piece(('img/destroyer2.png','img/croiseur2.png','img/sous-marin2.png','img/cuirassé2.png','img/porte_avions2.png'))
        img3=self.list_piece(('img/destroyer3.png','img/croiseur3.png','img/sous-marin3.png','img/cuirassé3.png','img/porte_avions3.png'))
        img4=self.list_piece(('img/destroyer4.png','img/croiseur4.png','img/sous-marin4.png','img/cuirassé4.png','img/porte_avions4.png'))
        return [img1,img2,img3,img4]

    def apparait(self):
        """ crée l'image """
        self.i=[]
        self.i.append(self.can.create_image(self.img[0][0],200,220))

    ### fin ###
### fin ###

### parametre de la fenetre et de la class et lancement classe/fonction ###
fen=Tk()
can=Canvas(fen,width=500,height=500,bg='black')
can.focus_set()
mvt=mouvement(can,20,20)
can.bind("<Button-3>",mvt.clic)
can.bind("<Button3-Motion>",mvt.reste)
can.bind("<MouseWheel>",mvt.suite)
fen.mainloop()
### fin ###