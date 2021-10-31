# Fonction qui choisit des éléments en fonction d'indice
def newlist(l1, l2):
    lst = []

# Les indices impairs de la première liste
    for i in range(len(l1)):
        if i%2 != 0:
            lst.append(l1[i])

# les indices pairs de la deuxième liste
    for i in range(len(l2)):
        if i%2 == 0:
            lst.append(l2[i])

    return lst

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
print("La première liste: ", l1, ", et la deuxième liste: ", l2)
# Affichage de la nouvelle liste
print("La nouvelle liste: ", newlist(l1, l2))

