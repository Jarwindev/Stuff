# Program som beräknar hur många gånger en boll studsar innan den stannar.

# Variabeln Studsantal används för att räkna antalet studsar.

Studsantal=0

# Användaren anger bollens höjd i meter.
# Om höjden är mindre än eller lika med 0, avslutas programmet.

Höjd=float(input("Höjd i meter: "))
if(Höjd <0):
    print("Programmet avslutas...")

    #Annars, om höjden är större än 0, beräknas antalet studsar.
    #Bollen når upp till 70% av sin tidigare höjd varje gång den studsar.

else:
    while(Höjd>0.01):
        Höjd=Höjd*0.7
        Studsantal=Studsantal+1

    # Antalet studsar skrivs ut.

    print("Bollen studsade:", Studsantal, "gånger.")
