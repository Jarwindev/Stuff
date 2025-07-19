# Program som beräknar summan av kvadraterna från 1 till n.

# Variabeln Kvadrat används för att lagra kvadraten av varje heltal i intervallet, 
# och variabeln Summa används för att lagra den totala summan.

Kvadrat=0
Summa=0

# Användaren anger ett heltal n, 

n=int(input("Heltal: "))

# och programmet beräknar summan av kvadraterna från 1 till n.

for i in range(1, n+1):
    Kvadrat=i*i
    Summa=Kvadrat+Summa

# Summan av kvadraterna skrivs ut.

print("Summan av kvadraterna från 1 till", n, "är:", Summa)