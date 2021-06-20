
from tkinter import *
from database import *
interface=Tk()
interface.title("Gestion de contact")

interface.geometry('1100x600')
interface.minsize(1150,600)
Label(interface,text="Gestion de mes contact",font=('Arial',35),bg='Gold',width=1100).pack(side=TOP, padx=5, pady=5)
# interface.iconbitmap("./gando.ico")

caneva=Canvas(interface,width=1000,height=550,bg='white')
caneva.pack(side=LEFT,padx=10)


Button(interface,text="ajouter",font=("Areal",15),).pack(side=TOP,padx=10,pady=30)
Button(interface,text="suprimer",font=("Areal",15)).pack()

        
contacts=recup_contact(connect())

for i in range(len(contacts)):
    for j in range(5):
        ligne=Entry(caneva, width=18, fg='blue',font=('Arial',16,'bold'))
        ligne.grid(row=i,column=j)
        ligne.insert(END,contacts[i][j])



interface.mainloop()