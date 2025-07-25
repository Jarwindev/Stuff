# Program som kontrollerar om ett brev är inom tillåtna mått för vanliga brev.

# Användaren anger brevets längd, bredd och tjocklek i millimeter.

Längd=int(input("Ange brevets längd i millimeter: "))
Bredd=int(input("Ange brevets bredd i millimeter: "))
Tjocklek=int(input("Ange brevets tjocklek i millimeter: "))

# Kontrollerar om brevets mått överskrider maxgränserna för vanliga brev, och meddelar om det är ogiltigt.

if Längd > 600 or (Bredd+Längd+Tjocklek)\
    > 900 or Tjocklek > 100:
    print("Brevets mått överskrider maxgränserna för vanliga brev.")

# Kontrollerar om brevets mått understiger minimi-kraven för vanliga brev, och meddelar om det är ogiltigt.

elif Längd < 140 or Bredd < 90:
    print("Brevets mått understiger minimi-kraven för vanliga brev.")

# Om brevets mått är inom tillåtna gränser, skrivs ut att det är giltigt.

else:
    print("Brevets mått är inom tillåtna gränser för vanliga brev.")