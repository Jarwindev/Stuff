# Program som beräknar värdet av en funktion för x-värden från -10 till 10.
# Värdet skrivs ut för varje x, med tre decimaler.

for x in range(-10, 11):
    Värde=(2*(x/10)**2-5*(x/10)+1)
    Värde=round(Värde, 3)
    print(Värde, end=", ")