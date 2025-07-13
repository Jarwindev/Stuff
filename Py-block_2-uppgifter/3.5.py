Längd=int(input("Ange brevets längd i millimeter: "))
Bredd=int(input("Ange brevets bredd i millimeter: "))
Tjocklek=int(input("Ange brevets tjocklek i millimeter: "))
if Längd > 600 or (Bredd+Längd+Tjocklek)\
    > 900 or Tjocklek > 100:
    print("Brevets mått överskrider maxgränserna för vanliga brev.")
elif Längd < 140 or Bredd < 90:
    print("Brevets mått understiger minimi-kraven för vanliga brev.")
else:
    print("Brevets mått är inom tillåtna gränser för vanliga brev.")