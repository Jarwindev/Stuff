import math

Vinkel = float(input("Ange vinkel i grader: "))
Sida_a = float(input("Ange längd på sida a: "))
Sida_b = float(input("Ange längd på sida b: "))

Sida_c = math.sqrt(Sida_a**2 + Sida_b**2 - 2 * Sida_a * Sida_b * math.cos(math.radians(Vinkel)))

if abs(Sida_a - Sida_b) < (10**-10) and abs(Sida_b - Sida_c) < (10**-10):
    print("Triangeln är liksidig.")

elif abs(Sida_a - Sida_b) <(10**-10) or abs(Sida_b - Sida_c) < (10**-10) or abs(Sida_a - Sida_c) < (10**-10):
    print("Triangeln är likbent.")
    
else:
    print("Triangeln är oliksidig.")