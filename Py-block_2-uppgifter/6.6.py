# Inte riktigt det som uppgiften efterfrågar, men ännu mer funktionell,
# eftersom den kan hantera olika antal rader och kolumner, och inte bara
# nxn som i uppgiften.
Rader=int(input("Ange antal rader i tabellen: "))
Kolumner=int(input("Ange antal kolumner i tabellen: "))
if(Rader < 1):
    print("Antal rader måste vara minst 1!")
else:
    if (Kolumner < 1):
        print("Antal kolumner måste vara minst 1!")
    else:
        for i in range(1,Rader+1):
            for j in range(1,Kolumner+1):
                print(f"{i * j:4}", end=" ")
            print()
