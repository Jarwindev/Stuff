
def versaler(_):
    text = input("Ange en text: ")
    små = sum(1 for c in text if c.islower())
    stora = sum(1 for c in text if c.isupper())
    return (små, stora)

print("Antal små respektive stora bokstäver:", versaler(""))
