Pris=float(input("Varans pris:"))
Momssats=float(input("Momssats i procent:"))/100
Moms=Momssats*Pris
Prisex=Pris-Moms
if(Moms%1==0):
    Moms=int(Moms)
if(Prisex%1==0):
    Prisex=int(Prisex)
print("Moms:", Moms, "kronor.")
print("Varans pris exklusive moms:", Prisex, "kronor.")

#Programmet räknar ut mängden moms på en vara, och priset exklusive denna baserat på bruttopriset och momssatsen.