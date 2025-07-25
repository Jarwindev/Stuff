# Program som läser in en matris rad för rad.

# Användaren matar in en matris rad för rad, och avslutar med en tom rad.

print("Mata in en matris rad för rad." \
" Avsluta med en tom rad.")

# Variabeln m används för att lagra matrisen.
# Varje rad läggs till som en lista av flyttal.

m=[]
while True:
    s=input("? ")
    if s == "":
        break
    ls = s.split(",")
    rad = [float(x) for x in ls]
    m.append(rad)
