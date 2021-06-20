count=0
nbrMax=None
while True:
    nbr=float(input("Entrer un nombre: "))
    if nbr==0:
        break
    count+=1
    if nbrMax is None or nbr>nbrMax :
        nbrMax=nbr
        countMax=count
if nbrMax is not None:
    print("le plus grand nombre est :",nbrMax,"avec le rang",countMax)
else:
     print("vous avez quitter le programme")
