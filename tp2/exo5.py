def minMaxMoy(b=[]):
    somme=0
    for i in b:
        somme+=i
    moyenne=somme/len(b)
    return max(b),min(b),moyenne
        