def nfak(n):
    if n < 0:
        return "Fakultet är inte definierad för negativa tal."
    elif n == 0 or n == 1:
        return 1
    else:
        resultat = 1
        for i in range(2, n + 1):
            resultat *= i
        return resultat

n = int(input("Ange ett heltal: "))
print("Fakulteten är:", nfak(n))

