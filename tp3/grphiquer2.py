from tkinter import*

# fenetre=Tk()
# fenetre.title("Bonjour Python")
# #taille d'affichage du fenetre
# fenetre.geometry('780x440')
# #pour modifier la taille du fenetre
# fenetre.maxsize(600,600)
# fenetre.minsize(300,300)
# # on poeut aussi interdire la modification de la taille du fenetre
# # fenetre.resizable(height=False,width=False)

# #widget

# # Bouton qui détruit la fenêtre
# button=Button(fenetre,text="quitter", command=fenetre.destroy)
# # insère le bouton dans la fenêtre
# button.pack(side="right")


# # creation de label
# texte=Label(fenetre, text="Hello World",font=("Areal",40))
# # Création du texte "Hello World" de couleur noire
# texte['fg']='blue' 
# # Insère le texte dans la fenêtre
# texte.pack() 


def repondre():
    affichage['text']=entrer.get()
    
windows=Tk()
windows.title("Exemple python")
windows.geometry('780x420')

texte=Label(windows,font=("Areal",45),text="Entrer votre text")
texte['fg']="blue"
texte.pack()

entrer=Entry(windows,width=40)
entrer.pack()


boutton=Button(windows,text="valider",command=repondre)
boutton.pack()

affichage=Label(windows,width=70)
affichage.pack()



# # On définit l'objet Entry qui porte le nom Entree
# Entree = Entry(fenetre)   
# # On place "Entree"  
# Entree.pack()              



windows.mainloop()
