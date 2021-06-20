from tkinter import*

fenetre=Tk()
fenetre.title("mon interface graphique")

fenetre.geometry('780x440')

texte=Label(fenetre,text="Siasisser quels chose",font=("Areal",49))
texte.pack()

def reponse():
    texte_saisi['text']=saisi.get()

saisi=Entry(fenetre,width=40)
saisi.pack()

bouton=Button(fenetre,text="valider",command=reponse)
bouton.pack()

texte_saisi=Label(fenetre)
texte_saisi.pack()

fenetre.mainloop()
