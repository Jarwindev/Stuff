# Program som letar efter det sista vita tecknet i en text.
# Det vita tecknet kan vara ett mellanslag eller en tabb.


# Användaren anger en text:

s = input("Skriv en text: ")

# Variabler för att hålla koll på positionen av det sista vita tecknet.

i = 0
d = -1

# Loopar igenom varje tecken i texten för att hitta det sista vita tecknet.
# Om ett vitt tecken hittas, uppdateras positionen.

for c in s:
    if c != " " and c != "\t":
        d = d + 1
    if c == " " or c == "\t":
        d = d + 1
        i = i + d
        d = 0

# Om ett vitt tecken hittades, skriv dess position ut.

if i > 0:
    print("Det sista vita tecknet är på position:", i)

# Om inga vita tecken hittas, skriv det ut.

else:
    print("Inga vita tecken i texten.")