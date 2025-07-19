# Programmet skapar en lista med ett visst mönster.

# En lista skapas med det första elementet 2.

Lista = [2]

# Variablerna n och k används för att skapa nästa element i listan.

n = 2
k = 3

# Användaren anger längden på listan, och programmet kontrollerar att den är minst 1.
# Om längden är mindre än 1, skrivs ett felmeddelande ut.

Längd=int(input("Ange längden på listan: "))
if(Längd < 1):
    print("Längden måste vara minst 1!")
else:

    # Programmet skapar nästa element i listan genom att multiplicera k med 3,
    # och lägger till det i listan.

    for i in range(Längd-1):
        n = 3*k
        Lista.append(n)

    # Programmet skriver ut den skapade listan.

    print(Lista)