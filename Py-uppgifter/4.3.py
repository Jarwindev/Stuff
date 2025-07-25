# Program som beräknar summan av inverserna från 1 till n.

# Variabeln Summa används för att lagra den totala summan av inverserna.
# Variabeln Kvot används för att lagra varje invers.

Summa=0
Kvot=0

# Användaren anger ett heltal n.

n=int(input("Heltal: "))

# Om n är mindre än eller lika med 0, skrivs ett felmeddelande ut.
# Annars beräknas summan av inverserna från 1 till n.

if n <= 0:
    print("Antalet måste vara ett positivt heltal.")
else:
    for i in range(1, n+1):
        Kvot=1/i
        Summa=Kvot+Summa

    # Summan av inverserna skrivs ut.

    print("Summan av inverserna från 1 till", n, "är:", Summa)