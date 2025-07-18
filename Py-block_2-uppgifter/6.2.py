n = 0
Lista=[]
Antal_tal=int(input("Ange antal tal: "))
for i in range(Antal_tal):
    tal = int(input("Ange tal: "))
    Lista.append(tal)
for tal in Lista:
    if tal < 0:
        n = n+1
print("Antalet negativa tal är:", n)