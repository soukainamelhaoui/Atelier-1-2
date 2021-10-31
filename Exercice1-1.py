# Calcul du factoriel
def fact(num):
    if num == 1:
        return 1
    else:
        return num*fact(num-1)

# Calcul de la somme
def sommeFact(n, func):
    somme = 0
    while n > 0:
        somme += func(n) / n
        n -= 1
    return somme

# Affichage de la somme de la série
print("Le résultat de la somme de la série: ",sommeFact(5, fact))