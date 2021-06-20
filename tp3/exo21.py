import datetime
# a) Date et heure actuelles

now = datetime.datetime.now()
print ("date courante est : ")
print (now.strftime("%H:%M:%S %d/%m/%Y "))
# b) Année en cours
print("Année en cours")
print(now.strftime("%Y"))
# c) Mois de l'année
print("Mois de l'année")
print(now.strftime("%b"))
# d) Jour du mois
print("jours du mois")
print(now.strftime("%d"))
# e) Numéro jour de la semaine
print("numero de semaine")
print(now.strftime("%W"))
# f) Jour de la semaine
print("le jour de la semaine")
print(now.strftime("%A"))