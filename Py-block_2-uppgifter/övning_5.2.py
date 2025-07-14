import datetime
dt = datetime.datetime.now()
d = dt.date()
Datum_bindestreck = str(d)
Datum=Datum_bindestreck.replace("-", "")
PN=input("Ange ett personnummer (10 siffror, inga bindestreck.): ")
if len(PN) == 10 and PN.isdigit():
    if (PN[2:6]) == Datum[4:8]:
        print("Grattis!")
else:
    print("Felaktigt personnummer.")

