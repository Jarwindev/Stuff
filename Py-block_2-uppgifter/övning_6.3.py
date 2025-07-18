s1=input("Ange element till en lista, separerade med kommatecken: ")
s2=input("Ange element till en tupel, separerade med kommatecken: ")
Lista=s1.split(",")
Tuple=tuple(s2.split(","))
j=0
for element in Lista:
        if element == Tuple[j]:
            j += 1
        else:
            print("Listan och tuplen är inte lika")
            break
if j == len(Tuple):
    print("Listan och tuplen är lika")