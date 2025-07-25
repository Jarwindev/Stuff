# Program för att beräkna det billigaste telefonabonnemanget baserat på uppskattat antal samtalsminuter.

# Tar in antal minuter som användaren uppskattar att den kommer att ringa.

Minuter=int(input("Ange antal uppskattade samtalsminuter: "))

# Kontrollerar om antalet minuter är negativt, noll eller inom olika intervall för att avgöra vilket abonnemang som är billigast.
# Skriver ut vilket abonnemang som är billigast baserat på användarens inmatning.

if Minuter < 0:
    print("Antalet minuter kan inte vara negativt.")
elif Minuter == 0:
    print("Inga samtal, ingen kostnad.")
elif Minuter <= 33:
    print("Billigast: Kontant.")
elif Minuter <= 66:
    print("Billigast: Normal.")
else:
    print("Billigast: Plus.")