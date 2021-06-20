class Domino:
    def __init__(self,a=0,b=0) :
        self.A=a
        self.B=b
    def affiche_points(self):
        print("face A : ",self.A," face B : ",self.B)
    def valeur(self):
        return self.A+self.B

d1=Domino(2,6)
d2=Domino(6,4)
d1.affiche_points()
d2.affiche_points()
print("sommme est: ",d1.valeur()+d2.valeur())