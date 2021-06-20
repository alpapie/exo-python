
import hashlib

vrais_mot_passe=b"alpapie"

hash_vrais_mote_passe=hashlib.md5(vrais_mot_passe).hexdigest()
f=open("C:/Users/user/Desktop/cours dev/python/exo python/mot_de_passe.txt","r")
for mot_de_pass in f:
    mot_de_passe=mot_de_pass.strip().encode('utf-8')
    mot_de_passe_chiffrer=hashlib.md5(mot_de_passe).hexdigest()
    if hash_vrais_mote_passe==mot_de_passe_chiffrer:
        print("le bon mot de passe est :",mot_de_pass)
        break
    else:
        print("maivais mot de passe")

# import qrcode
# import Image

# # example data
# data = "https://www.thepythoncode.com"
# # output file name
# filename = "./site.png"
# # generate qr code
# img = qrcode.make(data)
# # save img to a file
# img.save(filename)