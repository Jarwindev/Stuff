Text = input("Skriv en mening som ska översättas till rövarspråket: ")
Klartext = Text
for Bokstav in Text:
        if Bokstav.lower() in "bcdfghjklmnpqrstvwxyz":
            Text += Bokstav + "o" + Bokstav
        else:
            Text += Bokstav
Text = Text.removeprefix(Klartext)
print(Text)
