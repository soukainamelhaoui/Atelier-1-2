# Fonction qui vérifie si les éléments d'une liste existe dans un dictionnaire
def iter(L, dic):
    i = 0
    x = len(L)

#Itération de la liste
    while i < x-1:
        x = len(L)

# Si l'élément n'existe pas dans le dictionnaire on le supprime
        if L[i] not in dic.values():
            del L[i]
        else:
            i += 1
    return L

# Déclaration de la liste
L = [1, 2, 3, 7]
print("La liste avant la vérification: ", L)

# Déclaration di dictionnaire
dic = {"a" : 1, "b" : 5, "c" : 7 }
print("Le dictionnaire: ", dic)

# Affichage de la nouvelle liste
print("La nouvelle liste: ", iter(L, dic))