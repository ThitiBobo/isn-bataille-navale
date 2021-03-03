# Créé par Victorsd, le 08/05/2016 en Python 3.2
class partie:

    def __init__(self,j1,j2):
        self.j1=j1
        self.j2=j2
        self.T=1

    def attaque(self,event):
        x,y=event.X,event.Y
        if self.T==1:
            if j1[0]<x<j1[1] and <y<:
            self.T=2
        else:

            self.T=1


partie=partie([j1,158,169,46,10],[j2,822,169,46,10])


self.can.bind("<Button-1>",partie.attaque)