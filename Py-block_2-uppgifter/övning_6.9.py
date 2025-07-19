# Låter användaren mata in en vektor och beräknar dess längd.

# Vektorn matas in som en sträng med element separerade av kommatecken.

s=input("Mata in en vektor, element separerade med kommatecken: ")

# Delar upp strängen i en lista av element, konverterar varje element till float och beräknar längden av vektorn.
Vektor = [float(x) for x in s.split(",")]
Vektor_i_kvadrat = []
for element in Vektor:
    element_i_kvadrat = element ** 2
    Vektor_i_kvadrat.append(element_i_kvadrat)
Längd = sum(Vektor_i_kvadrat) ** 0.5

# Skriver ut längden av vektorn, avrundad till tre decimaler.
print("Längden av vektorn är:", round(Längd,3))
