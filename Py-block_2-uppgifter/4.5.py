Studsantal=0
Höjd=float(input("Höjd i meter: "))
if(Höjd <0):
    print("Programmet avslutas...")
else:
    while(Höjd>0.01):
        Höjd=Höjd*0.7
        Studsantal=Studsantal+1
    print("Bollen studsade:", Studsantal, "gånger.")
