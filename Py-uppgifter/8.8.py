def fyll(lista, övre, nedre, n):
    for i in range(len(lista)):
        if nedre <= lista[i] <= övre:
            lista[i] = n
    return lista

# Exempelanvändning:
a= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(fyll(a, 10, 5, 1))
