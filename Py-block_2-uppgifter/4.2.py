Kvadrat=0
Summa=0
n=int(input("Heltal: "))
for i in range(1, n+1):
    Kvadrat=i*i
    Summa=Kvadrat+Summa
print("Summan av kvadraterna från 1 till", n, "är:", Summa)