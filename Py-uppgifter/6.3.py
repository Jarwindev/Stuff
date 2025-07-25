# Programmet skapar en lista med 100 slumpmässiga tal mellan 1 och 1000,
# och beräknar det största, minsta och medelvärdet av dessa tal.

# Använder random-modulen för att generera slumpmässiga tal.

import random

# Skapar en tom lista för att lagra de slumpmässiga talen.

Lista = []

# Genererar 100 slumpmässiga tal mellan 1 och 1000 och lägger till dem i listan.
# Använder random.randint för att generera talen.

for i in range(100):
    n=random.randint(1, 1000)
    Lista.append(n)

# Beräknar det största och minsta talet i listan med hjälp av max() och min().
# Beräknar medelvärdet genom att summera alla tal och dela med antalet tal i listan.

Max= max(Lista)
Min= min(Lista)
Medelvärde = sum(Lista) / len(Lista)

# Skriver ut resultaten.

print("Det största talet är:", Max, "och det minsta talet är:", Min)
print("Medelvärdet är:", Medelvärde)

