# Program som översätter en mening till rövarspråket.

# Programmet tar in en mening från användaren och den i variabeln "Text".

Text = input("Skriv en mening som ska översättas till rövarspråket: ")

# Variabeln "Klartext" används för att lagra den ursprungliga meningen utan modifieringar.

Klartext = Text

# För varje bokstav i Text, om den är en konsonant, läggs "o" och bokstaven till efter den.
# Om den är en vokal, läggs den bara till som den är.

for Bokstav in Text:
        if Bokstav.lower() in "bcdfghjklmnpqrstvwxyz":
            Text += Bokstav + "o" + Bokstav
        else:
            Text += Bokstav

# Tar bort den ursprungliga meningen från Text, så att endast rövarspråket är kvar.
# Använder str.removeprefix() för att ta bort Klartext från början av Text.

Text = Text.removeprefix(Klartext)

# Skriver ut den översatta meningen i rövarspråket.

print(Text)
