def nfak(n):

    # Kollar först så att talet är positivt, annars returnerar felmeddelande.
    if n < 0:
        return "Fakultet är inte definierad för negativa tal."
    
    # Kollar sedan specialfallen 0 och 1, för vilka fakulteten är 1.
    elif n == 0 or n == 1:
        return 1
    
    # Annars körs den huvudsakliga delen av funktionen, for-loopen som för varje varv 
    # multiplicerar resultatet med räknaren och returnerar sedan resultatet.
    else:
        resultat = 1
        for i in range(2, n + 1):
            resultat *= i
        return resultat

# Användaren anger ett heltal och fakulteten skrivs då ut.
n = int(input("Ange ett heltal: "))
print("Fakulteten är:", nfak(n))