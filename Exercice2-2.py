# Division et inversion d'une liste en trois parties
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Votre liste avant la division: ", lst)

# vérification si la liste est divisable par trois
if len(lst)%3 == 0:
   n = int(len(lst)/3)

# Déclaration des trois nouvelles listes
   lst1 = lst[:n]
   lst2 = lst[n:2*n]
   lst3 = lst[2*n:3*n]

# L'inversion des nouvelles listes
   lst11 = lst1[::-1]
   lst12 = lst2[::-1]
   lst13 = lst3[::-1]

# L'affichage des trois nouvelles listes
   print("Les trois nouvelles listes: ",lst11, lst12, lst13)

# Le message à afficher si la liste n'est pas divisable sur tois
else:
    print("Votre liste ne peut pas etre déviser en trois.")


