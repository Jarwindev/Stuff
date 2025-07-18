import random
Lista = []
for i in range(100):
    n=random.randint(1, 1000)
    Lista.append(n)
Max= max(Lista)
Min= min(Lista)
print("Det största talet är:", Max, "och det minsta talet är:", Min)
Medelvärde = sum(Lista) / len(Lista)
print("Medelvärdet är:", Medelvärde)

