Summa=0
Kvot=0
n=int(input("Heltal: "))
if n <= 0:
    print("Antalet måste vara ett positivt heltal.")
else:
    for i in range(1, n+1):
        Kvot=1/i
        Summa=Kvot+Summa
    print("Summan av inverserna från 1 till", n, "är:", Summa)