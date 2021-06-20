import csv 
file = open("C:/Users/user/Desktop/cours dev/python/exo python/tp3//text.csv","r") 
reader = csv.reader(file , delimiter = ";") 
for line in reader : 
 print (line)
file.close ( ) 