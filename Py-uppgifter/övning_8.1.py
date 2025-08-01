prisex=int(input("Ange varans pris exklusive moms: "))
momssats=float(input("Ange varans momssats: "))

def pris_efter_moms(momssats,prisex):
    pris=prisex*(100+momssats)/100
    return pris

print("Varans pris inklusive moms är:", pris_efter_moms(momssats,prisex))