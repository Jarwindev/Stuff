# Program som skriver ut en nedåtgående triangel av plustecken.

# Användaren anger antalet rader.

n = int(input("Radantal? "))

# Skriver ut triangel med plustecken.

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("+", end=" ")
    print()