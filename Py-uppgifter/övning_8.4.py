# Användaren anger ett heltal.
n=int(input("Ange ett heltal (större än 0): "))

def primtal(n):

    # Räknaren j initieras till 0.
    j=0

    # Specialfall där n=1.
    if n==1:
        return True
    
    # För varje tall från 1 till n som n kan delas jämnt på, ökas räknaren j.
    for i in range(1,n):
        if n%i == 0:
            j+=1

    # Om j är lika med 1, returneras true, annars false.
    if j==1:
        return True
    else:
        return False           

# Om n är positivt kallas funktionen och användaren får reda på om n är ett primtal.
if n>0:

    if primtal(n):
        print("Talet är ett primtal.")
    else:
        print("Talet är inte ett primtal.")

# Annars skrivs ett felmeddelande ut.
else:
    print("Talet måste vara större än 0!")