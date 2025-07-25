# Program för att beräkna hur många dagar det tar att nå 10 miljoner i lön
# Lön börjar på 0.01 och fördubblas varje dag.

# Variabel Lön används för att lagra den aktuella lönen, och Dagar används för att räkna antalet dagar.

Lön=0.01
Dagar=0

# Loopar tills lönen når eller överstiger 10 miljoner.
# Varje iteration fördubblar lönen och ökar antalet dagar med 1

while(Lön<10000000):
    Lön=Lön*2
    Dagar+=1

# Skriver ut antalet dagar det tar att nå 10 miljoner i lön.

print("Det tar", Dagar, "dagar att nå 10 miljoner i lön.")