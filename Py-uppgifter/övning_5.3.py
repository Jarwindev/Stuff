# Program som kontrollerar om ett personnummer tillhör en man eller kvinna.

# Användaren matar in ett personnummer, och programmet kontrollerar det sista tecknet för att avgöra könet.
# Programmet skriver ut om personen är en man eller kvinna.

PN=input("Ange ett personnummer: ")
if int(PN[len(PN)-2:]) % 2== 0:
    print("Personen är kvinna.")
else:
    print("Personen är en man.")