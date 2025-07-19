# Programmet kollar om en text är ett palindrom.

# Användaren matar in en text, 

Text=input("Ange en text: ")

# och alla mellanslag tas bort för att jämförelsen ska vara korrekt.

New_Text=Text.replace(" ", "")

# Texten kontrolleras för att se om den är ett palindrom.
# Svaret skrivs ut baserat på jämförelsen.

if New_Text == New_Text[::-1]:
    print("Texten är ett palindrom.")
else:
    print("Texten är inte ett palindrom.")