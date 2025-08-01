# Användaren anger vad varans pris är exklusive moms och vad momssatsen är.
prisex=int(input("Ange varans pris exklusive moms: "))
momssats=float(input("Ange varans momssats: "))

def pris_efter_moms(momssats,prisex):

    # Priset räknas ut baserat på användarens input och returneras.
    pris=prisex*(100+momssats)/100
    return pris

# Skriver ut priset.
print("Varans pris inklusive moms är:", pris_efter_moms(momssats,prisex))