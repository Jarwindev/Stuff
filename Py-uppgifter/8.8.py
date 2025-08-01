def fyll(lista, övre, nedre, n):

    # För varje element i listan, om det är större än den nedre gränsen och 
    # mindre än den övre gränsen, så kommer det elementet att ersättas med n.
    for i in range(len(lista)):
        if nedre <= lista[i] <= övre:
            lista[i] = n

    # Returnerar listan efter eventuella ändringar:
    return lista

# Exempelanvändning av funktionen:
a= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(fyll(a, 10, 5, 1))
