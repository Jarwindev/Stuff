import math
def area_och_omkrets(radie):
    # Beräknar omkretsen av en cirkel med given radie.
    omkrets = 2 * math.pi * radie
    # Beräknar arean av en cirkel med given radie.
    area = math.pi * radie ** 2
    tupel = (omkrets, area)
    return tupel
radie = float(input("Ange radien på cirkeln: "))
print("Omkretsen av cirkeln är:", round(area_och_omkrets(radie)[0], 3))
print("Arean av cirkeln är:", round(area_och_omkrets(radie)[1], 3))