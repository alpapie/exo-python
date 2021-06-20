def moyenne(a=[]):
    somme=0
    for i in a:
        somme+=i
    return somme/len(a)

def afficher(moyene):
    if moyene>=10:
        print(moyen,"est suffisant pour passer en classe supérieure ")
    else:
        print(moyen,"est insuffisant pour passer en classe supérieure ")


notes=[]
while True:
    note=float(input("Entrer les notes "))
    if note <0:
        break
    notes.append(note)
moyen=moyenne(notes)
afficher(moyen)