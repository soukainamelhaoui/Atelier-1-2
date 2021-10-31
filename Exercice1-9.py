# Fonction qui calcul la position d'un élément
def matrice(L, x):
    pos = ""
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] == x:
                pos += "<< " + str(i) + ", " + str(j) + " >>"
                return pos

element = 3
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Affichage de la position d'un élément
print ("La position de ",element, "est ", matrice(L, element))