# Fonction qui inverse une chaine de caractères
def reverse(word1):
    word2 = ""
    for i in range(len(word1)-1, 0, -1):
        word2 += word1[i]
    word2 += word1[0]

    return word2

# Affichage de la chaine de caractères après l'inversion
word = "Heyy"
print("Le mot ",word,"après l'inversion est: ",reverse(word))