# Fonction qui calcul le nombre d'occurrence d'un élément
def dicList(lst):
    dct = {}
    for i in range(len(lst)-1):
        c = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                c += 1
        dct[lst[i]] = c
    return dct

l = [1, 2, 2, 3, 4, 3, 2, 1, 5]

# Affichage du dictionnaire contenant les éléments de la liste et leurs nombres d'occurrence
print("Les éléments de votre liste et leurs nombres d'occurrence: ",dicList(l))

