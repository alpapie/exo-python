liste =[17, 38, 10, 25, 72, 15, 36, 87]

#1)trie du tableau
liste.sort()
print(liste)

#2)ajout dans le tableau
liste.append(12)
print(liste)

#3)reverse du liste
liste.reverse()
print(liste)

#4)affichde l'element 25
indice=liste.index(25)
print(indice)

#5)enlevons 15
liste.pop(liste.index(15))
print(liste)

#6)sous liste 2éme 
print(liste[2:6])

#7)sous-liste 
print(liste[:4])

#8)sous-liste 3 a la fin
print(liste[3:])

#affichage de l'avant dernier element
print(liste[-2])