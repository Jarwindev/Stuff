# Programmet räknar antalet negativa tal i en lista.

# Variabel n används för att räkna antalet negativa tal.
# Lista används för att lagra de inmatade talen.

n = 0
Lista=[]

# Användaren anger hur många tal som ska matas in.

Antal_tal=int(input("Ange antal tal: "))

# Programmet tar in talen ett i taget och lägger till dem i listan.
# Om ett tal är negativt, ökas räknaren n med 1.

for i in range(Antal_tal):
    tal = int(input("Ange tal: "))
    Lista.append(tal)
for tal in Lista:
    if tal < 0:
        n = n+1

# Skriver ut antalet negativa tal.

print("Antalet negativa tal är:", n)