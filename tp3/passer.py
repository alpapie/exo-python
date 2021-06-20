def moyenne(a=[]):
    somme=0
    for i in a:
        somme+=i
    return somme/len(a)

def afficher(moyen):
    if moyen>=10:
        print(moyen,"est suffisant pour passer en classe supérieure ")
    else:
        print(moyen,"est insuffisant pour passer en classe supérieure ")

