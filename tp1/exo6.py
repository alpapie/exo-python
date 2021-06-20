nbrcopie=int(input("Entrer le nombre de photocopie a effectue: "))
if nbrcopie<=10:
    prix=nbrcopie*35
elif nbrcopie<=30:
    prix=((nbrcopie-10)*25)+(10*35)
else:
    prix=((nbrcopie-30)*15)+(20*25)+(10*35)
print("pour une photocopie de",nbrcopie,"page sa vous coutera",prix)
