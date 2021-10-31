# Fonction qui calcul le nombre d'occurrence d'un nombre
def frequence(word, x):
    c = 0
    for i in range(len(word)):
        if x in word[i]:
            c += 1

    return c
x = "y"
word = "heyy"

# Affichage du nombre d'occurrence d'un caractère
print ("L'element ", x, "est ", frequence(word, x), "fois dans votre chaine de caractre", word)