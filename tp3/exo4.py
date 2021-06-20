f=open("C:/Users/user/Desktop/cours dev/python/exo python/tp3/text.txt","w")
i=10
while i>1:
    f.write("ahmadou n'\ a pas fait ses exos tp3\n")
    i=i-1
f.close()


f=open("C:/Users/user/Desktop/cours dev/python/exo python/tp3/text.txt","r")
for x in f:
  print(x)
