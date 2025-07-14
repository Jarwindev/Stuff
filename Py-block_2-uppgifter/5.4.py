s = input("Skriv en text: ")
i = 0
d = -1
for c in s:
    if c != " " and c != "\t":
        d = d + 1
    if c == " " or c == "\t":
        d = d + 1
        i = i + d
        d = 0
if i > 0:
    print("Det sista vita tecknet är på position:", i)
else:
    print("Inga vita tecken i texten.")