Minuter=int(input("Ange antal uppskattade samtalsminuter: "))
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