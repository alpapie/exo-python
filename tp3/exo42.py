f=open("./text2.txt","w")
i=10
while i>1:
    f.write("ahmadou n'a pas fait ses exos tp3\n")
    i=i-1
f.close()
f=open("./text2.txt","r")
for line in f:
    print(line)
f.close()