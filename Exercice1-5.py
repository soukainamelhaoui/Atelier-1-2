# Calcul du nombre des chiffres d'un nombre
def nombreChiff(num):

    if num <= 1:
        return 1
    else:
        return 1 + nombreChiff(num // 10)

# Affichage du nombre des chifres d'un nombre
num = 135
print("Le nombre des chiffres dans ", num, " est: ", nombreChiff(num))