# Programmet skapar en multiplikationstabell med angivet antal rader och kolumner.
# Inte riktigt det som uppgiften efterfrågar, men ännu mer funktionell,
# eftersom den kan hantera olika antal rader och kolumner, och inte bara
# n*n som i uppgiften.

# Användaren anger antal rader och kolumner, och programmet kontrollerar att de är minst 1.
# Om inte, felmeddelanden ut.

Rader=int(input("Ange antal rader i tabellen: "))
Kolumner=int(input("Ange antal kolumner i tabellen: "))
if(Rader < 1):
    print("Antal rader måste vara minst 1!")
else:
    if (Kolumner < 1):
        print("Antal kolumner måste vara minst 1!")

    # Om både rader och kolumner är giltiga, skapas multiplikationstabellen.
    # Programmet skriver ut tabellen med ett snyggt format.

    else:
        for i in range(1,Rader+1):
            for j in range(1,Kolumner+1):
                print(f"{i * j:4}", end=" ")
            print()
