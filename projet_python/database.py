import  mysql.connector

def connect(host="localhost",user="root",password="",database="contacts_py"):
    connexion = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
    port=3306)
    return connexion

def recup_contact(connetion,request="SELECT * FROM personnes_py"):
    
    connexion=connetion
    curseur = connexion.cursor()
    curseur.execute(request)
    contacts=curseur.fetchall()
    return contacts
def ajouter_contact():
    request=""
contacts=recup_contact(connect())

# for contact in contacts:
#     contacte=str(contact[0])+" "+contact[1]+" "+contact[2]+" "+contact[3]+" "+str(contact[4])+" "
#     print(contacte)