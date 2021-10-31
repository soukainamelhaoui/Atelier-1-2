# Fonction qui cherche l'intersection des deux Sets
def intersect(set1, set2):
    set3 = set1.intersection(set2)
    return set3

# Déclaration des Sets
x = {"one", "two", "three"}
y = {"three", "four", "five"}
print("Le premier set: ",x, ", Le deuxième set: ", y)

# L'affichage des élement communs entre deux Sets
print("Les élements communs des deux sets: ",intersect(x, y))