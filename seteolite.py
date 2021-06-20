class Satellite():
    def __init__(self,nom,masse = 100, vitesse = 0):
        self.masse=masse
        self.vitesse=vitesse
        self.nom=nom
    def impulsion(self,force, duree):
        self.vitesse=self.vitesse+ (force*duree)/self.masse
    def affiche_vitesse(self):
        print("le satelite",self.nom,"a une vitesse de",self.vitesse,"m/s" )
    def energie(self):
        return 0.5*self.masse*self.vitesse**2
        
    
    
s1 = Satellite('Zoé', masse =250, vitesse =10)
s1.impulsion(500, 15)
s1.affiche_vitesse()
print( s1.energie())