def är_perfekt(n):
    summa = 0
    # Loopar igenom alla tal från 1 till n-1 för att hitta delare.
    for i in range(1, n):
        if n % i == 0:  # Om i är en delare av n.
            summa += i  # Lägg till delaren i summan.
    return summa == n  # Returnera True om summan av delarna är lika med n, annars False.
n = int(input("Ange ett heltal: "))
if är_perfekt(n):
    print(n, "är ett perfekt tal.")
else:
    print(n, "är inte ett perfekt tal.")