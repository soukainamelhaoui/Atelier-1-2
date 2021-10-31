# Calcul de la somme de 1 à n en utilisant la récursivité
def sommeRecursive(num):
    if num == 1:
        return 1
    else:
        return num+sommeRecursive(num-1)

# Affichage de la somme calculée
num = 4
print("La somme des nombres de 1 à ", num, " est: ",sommeRecursive(num))