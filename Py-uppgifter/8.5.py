def är_perfekt(n):

    # Initierar summa till 0.
    summa = 0

    # Loopar igenom alla tal från 1 till n-1 för att hitta delare.
    for i in range(1, n):
        if n % i == 0:  # Om i är en delare av n.
            summa += i  # Lägg till delaren i summan.
    return summa == n  # Returnera True om summan av delarna är lika med n, annars False.

# Användaren anger ett heltal.
n = int(input("Ange ett heltal: "))

# Funktionen anropas och användaren får reda på om talet är perfekt eller inte.
if är_perfekt(n):
    print(n, "är ett perfekt tal.")
else:
    print(n, "är inte ett perfekt tal.")