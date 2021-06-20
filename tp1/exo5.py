tempEau=float(input("entrer la temperature de l'eau: "))
if tempEau<=0 :
     print("etat solide de l'eau")
elif 0<tempEau<100:
    print("etat liquide de l'eau")
elif tempEau >=100 :
    print("etat gazeux de l'eau")