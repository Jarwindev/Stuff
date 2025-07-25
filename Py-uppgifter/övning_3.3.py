# Programmet beräknar längden på den tredje sidan i en triangel baserat på två sidor och vinkeln mellan dem.
# Det avgör också vilken typ av triangel det är: liksidig, likbent eller oliksidig.

# Importerar math-modulen för att använda matematiska funktioner.

import math

# Tar in vinkel i grader och längder på de två sidorna som bildar vinkeln.

Vinkel = float(input("Ange vinkel i grader: "))
Sida_a = float(input("Ange längd på sida a: "))
Sida_b = float(input("Ange längd på sida b: "))

# Beräknar längden på den tredje sidan med hjälp av cosinusregeln.

Sida_c = math.sqrt(Sida_a**2 + Sida_b**2 - 2 * Sida_a * Sida_b * math.cos(math.radians(Vinkel)))

# Avgör vilken typ av triangel det är baserat på längderna på sidorna.

if abs(Sida_a - Sida_b) < (10**-10) and abs(Sida_b - Sida_c) < (10**-10):
    print("Triangeln är liksidig.")

elif abs(Sida_a - Sida_b) <(10**-10) or abs(Sida_b - Sida_c) < (10**-10) or abs(Sida_a - Sida_c) < (10**-10):
    print("Triangeln är likbent.")
    
else:
    print("Triangeln är oliksidig.")