from personne import Personne

class Professeur(Personne):
    allModules={'dwm' : ['python','Java','php'],'asr':['linux','maintenance','routage']}
    def __init__(self,modules,age,nom):
        super().__init__(age,nom)
        self._modules=modules
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        if age>=16:
            self._age=age
        else:
            raise("l'age doit etre superieur ou egale a 16")
        
    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self,nom):
        if len(nom)>=6:
          self._nom=nom
        else:
            raise("Votre nom doit etre superieur a 6 caractere")
        
         

    @property
    def modules(self):
        return self._modules
    @modules.setter
    def modules(self,newmodules):
        if newmodules in Professeur.allModules:
            self._modules=newmodules
        else:
            print("ce module ne correspond pas")
            
    def __str__(self):
        return "Je suis un fprofesseur qui s'appelle "+self._nom+" agé de "+str(self._age)+" ans et mes modules sont "+self._modules