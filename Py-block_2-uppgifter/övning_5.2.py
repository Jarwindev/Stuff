# Program som kontrollerar om ett personnummer är giltigt och gratulerar personen om det är hens födelsedag.
# Det kontrollerar om personnumret är 10 siffror långt och om det matchar det aktuella datumet.

# Importerar datetime för att hämta dagens datum.
# Använder datetime för att få det aktuella datumet i formatet YYYYMMDD.

import datetime
dt = datetime.datetime.now()
d = dt.date()

# Formaterar datumet till en sträng utan bindestreck med replace.

Datum_bindestreck = str(d)
Datum=Datum_bindestreck.replace("-", "") 

# Tar in ett personnummer från användaren.

PN=input("Ange ett personnummer (10 siffror, inga bindestreck.): ")

# Kontrollerar om personnumret är 10 siffror långt och om det är giltigt.
# Om det är giltigt, kontrollerar det om det är personens födelsedag.
# Om det är personens födelsedag, gratulerar programmet användaren.

if len(PN) == 10 and PN.isdigit():
    if (PN[2:6]) == Datum[4:8]:
        print("Grattis!")
else:
    print("Felaktigt personnummer.")

