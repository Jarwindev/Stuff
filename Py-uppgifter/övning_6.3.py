# Program som jämför en lista och en tupel för att se om de är lika.

# Användaren matar in en lista och en tupel. 

s1=input("Ange element till en lista, separerade med kommatecken: ")
s2=input("Ange element till en tupel, separerade med kommatecken: ")

# Delar upp strängarna i en lista och en tupel.

Lista=s1.split(",")
Tuple=tuple(s2.split(","))

# Variabeln j används för att hålla koll på index i tuplen.

j=0

# Programmet kontrollerar om de har samma element i samma ordning.

for element in Lista:
        if element == Tuple[j]:
            j += 1
        else:
            print("Listan och tuplen är inte lika")
            break

# Om alla element i listan matchar tuplen, och om de har samma längd, skrivs det ut att de är lika.

if j == len(Tuple):
    print("Listan och tuplen är lika")