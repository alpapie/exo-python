phrase=input("entrer votre phrase: ")
tabmot=phrase.split()
print("Le nombre de mot est de",len(tabmot))

maxmot=''
tabmaxmot=[]
for mot in tabmot:
    if len(mot)>len(maxmot):
        maxmot=mot
for grandmot in tabmot:
    if len(grandmot)==len(maxmot):
        tabmaxmot.append(grandmot)
print("le mot le plus long est : ",tabmaxmot)




#for indice in range(0,len(maxmot)):
#     for mot in tabmot:
#         if len(mot)==len(maxmot[indice]):
#             maxmot.append(mot)
#         if len(mot)>len(maxmot[indice]):
#             maxmot[indice]=mot
# print("le mot le plus long est : ",maxmot)