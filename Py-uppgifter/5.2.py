# Program som kontrollerar om första och sista tecknet i en text är lika.

# Användaren anger en text och programmet jämför första och sista tecknet.

Text=input("Ange en text:")
if Text[0] == Text[len(Text)-1]:
    print("Första och sista tecknet är lika.")
else:
    print("Första och sista tecknet är inte lika.")