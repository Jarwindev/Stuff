romerskt_tal=input("Mata in ett romerskt tal: ").upper()
romerska_tal_tabell = {
    "I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000
}

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
print("Det arabiska talet är:", romerskt_tal_till_arabiskt(romerskt_tal))
