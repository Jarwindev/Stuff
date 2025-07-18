Lista = [2]
n = 2
k = 3
Längd=int(input("Ange längden på listan: "))
if(Längd < 1):
    print("Längden måste vara minst 1!")
else:
    for i in range(Längd-1):
        n = 3*k
        Lista.append(n)
    print(Lista)