listeValeur=[]

while True:
    nbr=int(input('Veuillez entrer un nombre'))
    if nbr==0 :
        break
    listeValeur.append(nbr)
plusGrand=max(listeValeur)
rangPlusGrand=listeValeur.index(plusGrand)+1
print("le plus grand nombre de la liste est:",plusGrand,"avec comme rang",rangPlusGrand)
