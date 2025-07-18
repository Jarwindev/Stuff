s=input("Mata in en vektor, element separerade med kommatecken: ")
Vektor = [float(x) for x in s.split(",")]
Vektor_i_kvadrat = []
for element in Vektor:
    element_i_kvadrat = element ** 2
    Vektor_i_kvadrat.append(element_i_kvadrat)
Längd = sum(Vektor_i_kvadrat) ** 0.5
print("Längden av vektorn är:", round(Längd,3))
