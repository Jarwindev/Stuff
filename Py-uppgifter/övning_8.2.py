# Användaren anger ett heltal.
n=int((input("Ange ett heltal: ")))

def multipler(n):

    # Om n är utanför intervallet blir användaren varse om det.
    if n<1 or n>10:
        print("Talet n måste vara mellan 1 och 10!")

    # Annars körs en for-loop som skriver ut n-multiplerna mellan 1 och 10.    
    else:
        for i in range(1,11):
            print(i, i*n)

# Funktionen kallas.       
multipler(n)