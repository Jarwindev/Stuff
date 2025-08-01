from math import factorial

x=float(input("Ange ett tal: "))
n=int(input("Ange antal termer: "))

def Maclaurin(x, n):

    resultat = 0
    
    for k in range(n):
        term = (x ** k) / factorial(k)
        if term > 0.0000001:
            resultat += term
            
    return resultat

print("Maclaurin-serien för e^x med", n, "termer är:", Maclaurin(x, n))
