class Personne:
    def __init__(self,age,nom):
        self._age=age
        self._nom=nom
    def __str__(self):
        return "Je suis  "+self._nom+" agé de "+str(self._age)
    