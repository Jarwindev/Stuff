# Funktionen använder inga parametrar utifrån.
def versaler(_):

    # Användaren anger en text.
    text = input("Ange en text: ")

    # Textens stora och små bokstäver räknas och både dessa summor returneras.
    stora = sum(1 for c in text if c.isupper())
    små = sum(1 for c in text if c.islower())
    return (stora,små)

# Antalet stora respektive små bokstäver skrivs ut.
print("Antal stora respektive små bokstäver:", versaler(""))