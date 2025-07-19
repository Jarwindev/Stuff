# Programmet kontrollerar om en matris är en magisk fyrkant.

# En tom lista för att lagra matrisen.

m=[]

# Tar in matrisen rad för rad, där varje rad är en sträng med element separerade av kommatecken.

print("Mata in en matris rad för rad. Avsluta med en tom rad.")

# Användaren kan mata in flera rader tills de lämnar en tom rad.
while(input != ""):
    s=input("? ")
    if s == "":
        break
    ls = s.split(",")
    rad = [float(x) for x in ls]
    m.append(rad)

# Variabel n används för att lagra summan av den första raden, som används för att jämföra med andra rader och kolumner.
# Variabel y används för att räkna antalet rader som är lika med n.    

n = sum(rad)
y = 0

# Kontrollerar rader

for rad in m:
    if sum(rad) == n:
        y += 1
    else:
        print("Raderna är inte lika")
        break

# Om alla rader är lika, och om längden stämer skrivs ut att raderna är lika.

if y == len(m):
    print("Alla rader är lika") 

    # Kontrollerar kolumner, och skriver ut svar.

    for col in range(len(m[0])):
        if sum(row[col] for row in m) != n:
            print("Kolumnerna är inte lika")
            break
        else:
            print("Alla kolumner är lika")
            y += 1
            break

            # Kontrollerar diagonaler och skriver ut svar.

    if sum(m[i][i] for i in range(len(m))) == n and sum(m[i][len(m)-1-i] for i in range(len(m))) == n:
        y += 1
        print("Båda diagonalerna är lika")
    else:
        print("Diagonalerna är inte lika")

# Om alla rader, kolumner och diagonaler är lika, skrivs ut att matrisen är en magisk fyrkant.

if y == len(m) + 2:
    print("Matrisen är en magisk fyrkant")
else:
    print("Matrisen är inte en magisk fyrkant")