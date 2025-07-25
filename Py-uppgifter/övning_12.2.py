# Tar in ett romerskt tal och konverterar det till uppercase.

romerskt_tal=input("Mata in ett romerskt tal: ").upper()

# Ordbok för att konvertera romerska tal till arabiska tal.

romerska_tal_tabell = {
    "I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000
}
# Funktion för att konvertera romerska tal till arabiska tal genom att iterera över varje symbol i det romerska talet.
# Om den nuvarande symbolen är mindre än den tidigare symbolen subtraheras dess värde från totalen, annars adderas det.
# Returnerar det totala värdet av det arabiska talet.

def romerskt_tal_till_arabiskt(romerskt_tal):
    total = 0
    tidigare_värde = 0
    for symbol in reversed(romerskt_tal):
        värde = romerska_tal_tabell[symbol]
        if värde < tidigare_värde:
            total -= värde
        else:
            total += värde
        tidigare_värde = värde
    return total

# Anropar funktionen och skriver ut resultatet.

print("Det arabiska talet är:", romerskt_tal_till_arabiskt(romerskt_tal))
