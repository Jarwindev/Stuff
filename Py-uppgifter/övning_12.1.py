# Skrev ihop båda funktionerna för att översätta mellan Morse-kod och klartext
# i samma fil för att är mer effektivt. Inkluderade även siffror.

# Funktion för att hantera översättning mellan Morse-kod och klartext.
# Använder en avbildningstabell för att lagra Morse-koden och dess motsvarande tecken.

def main():
    morse_alfa = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", 
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", 
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", 
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", 
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", 
        "Z": "--..", "Å": ".--.-", "Ä": ".-.-", "Ö": "---.",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", 
        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    }

    # Inverterar avbildningstabellen för att kunna översätta från Morse-kod till klartext.
    # Nycklar blir värden och värden blir nycklar.

    morse_till_text = {v: n for n, v in morse_alfa.items()}

    # Användargränssnitt för att välja översättningstyp.
    # Tar in ett val från användaren för att bestämma om de vill översätta till Morse-kod eller klartext.
    # Om användaren väljer 1, tar den in en textsträng och översätter den till Morse-kod.
    # Om användaren väljer 2, tar den in en Morse-kod och översätter den till klartext.
    # Om användaren väljer något annat, skriver den ut ett felmeddelande.

    val = input("1. Översätt till Morse-kod\n2. Översätt till Klartext\nVälj: ")
    if val == "1":
        text = input("Mata in text att översätta till Morse-kod: ").upper()
        morse_kod = " ".join(morse_alfa[bokstav] for bokstav in text if bokstav in morse_alfa)
        print("Morse-kod:", morse_kod)
    elif val == "2":
        morse_kod = input("Mata in Morse-kod att översätta till klartext (separera med mellanslag): ")
        text = "".join(morse_till_text[kod] for kod in morse_kod.split() if kod in morse_till_text)
        print("Klartext:", text)
    else:
        print("Ogiltigt val, vänligen välj 1 eller 2.")

# Anropar huvudfunktionen för att starta programmet.

if __name__ == "__main__":
    main()