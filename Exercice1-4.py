# Calcul du nombre fibonacci de la position n en utilisant la récursivité
def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return  fibonacci(n-1) + fibonacci(n-2)

# Fonction d'affichage de la série du Fibonacci
def fibonaccii(n, func):
    while n > 0:
        print (func(n))
        n -= 1
    return 0

# Affichage de la série de fibonacci
print(fibonaccii(7, fibonacci))