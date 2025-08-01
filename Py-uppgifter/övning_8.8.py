# Importerar factorial från math.
from math import factorial

# Användaren anger det tal som e ska upphöjas till och hur många termer som ska ingå i serien.
x=float(input("Ange ett tal: "))
n=int(input("Ange antal termer: "))

def Maclaurin(x, n):
    
    # Resultat initieras till 0.
    resultat = 0
    
    # För varje tal k i n, bildas en term i serien med hjälp av k.
    for k in range(n):
        term = (x ** k) / factorial(k)

        # Om denna term är större en -10^7 adderas den till resultatet, annars inte,
        # eftersom den då inte skulle ha någon större inverkan på resultatet.
        if term > 0.0000001:
            resultat += term

    # Resultatet av beräkningen returneras.        
    return resultat

# Kollar om n är mindre än 1, då skrivs ett felmeddelande ut.
if n<1:
    print("Åtminstone en term behövs!")

# Annars kallas funktionen och resultatet skrivs ut.    
else:
    print("Maclaurin-serien för e^x med", n, "termer är:", Maclaurin(x, n))