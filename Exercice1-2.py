# Fonction qui convertit un nombre décimal en binaire
def binaire(num):
    l = []
    l2 = []
    strin = ""

# Conversion en binaire sous forme d'une liste
    while num>0:
        l.append(num%2)
        num = num//2
    l2 = l[::-1]

# Conversion de la liste en une chaine de charactères
    for i in range(len(l2)):
        strin += str(l2[i])
    return strin

# Affichage du nombre binare
num = 210
print("Le nombre ",num, " en binaire est: ",binaire(num))




