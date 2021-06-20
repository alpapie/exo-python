# a) Date et heure actuelles
import datetime
now = datetime.datetime.now()
print ("date courante est : ")
print (now.strftime("%H:%M:%S %d/%m/%Y "))
# b) Année en cours
print("l'anne courant")
print(now.strftime("%Y"))
# c) Mois de l'année
print("le mois de l'anne")
print(now.strftime("%m"))
# d) Jour du mois
print("le jour du mois")
print(now.strftime("%d"))
# e) Numéro jour de la semaine
print("le numero de semaine")
print(now.strftime("%w"))
# f) Jour de la semaine
print("le jours")
print(now.strftime("%A"))


# from datetime import date, time, datetime
# aujourdhui=date.today()
# # a) Date et heure actuelles
# print("Aujourd'hui nous somme le : ",aujourdhui)
# # b) Année en cours
# print("L'année courant c'est : ",aujourdhui.year)
# # c) Mois de l'année
# print("Le mois courant c'est : ",aujourdhui.month)
# # d) Jour du mois
# print("Aujourd'hui c'est : ",aujourdhui.day)
# # e) Numéro jour de la semaine
# print("Le numéro numéro de jour de la semaine : ",aujourdhui.weekday())
# # f) Jour de la semaine