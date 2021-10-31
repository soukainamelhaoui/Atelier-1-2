lst = [7, 1, 5, 6, 3, 8]

# Affichage de la liste avant le tri
print("Le tableau avant le tri: ", lst)

# Fonction du tri par insertion
def tri_par_insertion(L):
    for i in range(len(L)-1):
        for j in range(i, len(L)):
            x = L[j]
            if L[i] > L[j]:
                L[j] = L[i]
                L[i] = x

    return L

# Affichage de la liste après le tri par insertion
print("Le tableau après le tri par insertion: ", tri_par_insertion(lst))

# Fonction du tri par selection
def tri_par_selection(L):
    for i in range(len(L)):
        min = i
        for j in range(i, len(L)):
            if L[min] > L[j]:
                min = j

        x = L[i]
        L[i] = L[min]
        L[min] = x

    return L

# Affichage de la liste après le tri par selection
print("Le tableau après le tri par selection: ",tri_par_selection(lst))

# Fonction du tri à bulle
def tri_a_bulle(L):
    for i in range(len(L)):
        for j in range(len(L)-i-1):
            x = L[j]
            if L[j] > L[j+1]:
                L[j] = L[j+1]
                L[j+1] = x
    return L

# Affichage de la liste après le tri à bulle
print("Le tableau après le tri à bulle: ",tri_a_bulle(lst))

