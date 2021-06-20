from personne import Personne
class Apprenant(Personne):
    metiers=['dwm','asr','rta','er']
    def __init__(self,metier,age,nom):
        Personne.__init__(self,age,nom)
        self._metier=metier
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        if age>=16:
            self._age=age
        else:
            print("l'age doit etre superieur ou egale a 16")
        
    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self,nom):
        if len(nom)>=6:
          self._nom=nom
        else:
            print("Votre nom doit etre superieur a 6 caractere")
        
         

    @property
    def metier(self):
        return self._metier
    @metier.setter
    def metier(self,newMetier):
        if newMetier in Apprenant.metiers:
            self._metier=newMetier
        else:
            print("ce metiers ne correspond pas")
    def __str__(self):
        return "Je suis un apprenant qui s'appelle "+self._nom+" agé de "+str(self._age)+" ans et mon métier est "+self._metier