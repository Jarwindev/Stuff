# Skrev ihop båda funktionerna för att översätta mellan Morse-kod och klartext
# i samma fil för att är mer effektivt.
# Använder en ordbok för att lagra Morse-koden och dess motsvarande tecken. 

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
    morse_to_text = {v: k for k, v in morse_alfa.items()}

    val = input("1. Översätt till Morse-kod\n2. Översätt till Klartext\nVälj: ")
    if val == "1":
        text = input("Mata in text att översätta till Morse-kod: ").upper()
        morse_kod = " ".join(morse_alfa[bokstav] for bokstav in text if bokstav in morse_alfa)
        print("Morse-kod:", morse_kod)
    elif val == "2":
        morse_kod = input("Mata in Morse-kod att översätta till klartext (separera med mellanslag): ")
        text = "".join(morse_to_text[kod] for kod in morse_kod.split() if kod in morse_to_text)
        print("Klartext:", text)
    else:
        print("Ogiltigt val, vänligen välj 1 eller 2.")

if __name__ == "__main__":
    main()