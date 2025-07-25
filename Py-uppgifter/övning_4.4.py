# Programmet skriver ut en multiplikationstabell för talen 1 till 9.
# Varje rad i tabellen representerar produkten av ett tal från 1 till 9 med varje tal från 1 till 9.

for i in range(1,10):
    for j in range(1,10):

        # Skriver ut produkten av i och j, med ett format som gör att varje tal tar upp 4 tecken.
        # Detta gör att tabellen blir snyggt justerad.

        print(f"{i * j:4}", end=" ")
    print()