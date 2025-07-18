m=[]
print("Mata in en matris rad för rad. Avsluta med en tom rad.")
while(input != ""):
    s=input("? ")
    if s == "":
        break
    ls = s.split(",")
    rad = [float(x) for x in ls]
    m.append(rad)
n = sum(rad)
y = 0
for rad in m:
    if sum(rad) == n:
        y += 1
    else:
        print("Raderna är inte lika")
        break
if y == len(m):
    print("Alla rader är lika")
    # Kontrollera kolumner
    for col in range(len(m[0])):
        if sum(row[col] for row in m) != n:
            print("Kolumnerna är inte lika")
            break
        else:
            print("Alla kolumner är lika")
            y += 1
            break
            # Kontrollera diagonaler
    if sum(m[i][i] for i in range(len(m))) == n and sum(m[i][len(m)-1-i] for i in range(len(m))) == n:
        y += 1
        print("Båda diagonalerna är lika")
    else:
        print("Diagonalerna är inte lika")
if y == len(m) + 2:
    print("Matrisen är en magisk fyrkant")