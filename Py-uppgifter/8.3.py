def siff_antal(n):
    i = 0
    while n > 0:
        i += 1      # Ökar räknaren i med 1 för varje siffra.
        n //= 10         # Tar bort den sista siffran från n.
    return i

# Anropar funktionen med användarens inmatning, skriver ut resultatet.

print("Antalet siffror är:", siff_antal(int(input("Ange ett heltal: "))))