import math
def omkrets(radie):
    # Beräknar omkretsen av en cirkel med given radie.
    return 2 * math.pi * radie
def area(radie):
    # Beräknar arean av en cirkel med given radie.
    return math.pi * radie ** 2
radie = float(input("Ange radien på cirkeln: "))
print("Omkretsen av cirkeln är:", round(omkrets(radie),3))
print("Arean av cirkeln är:", round(area(radie),3))