def medelvärde(s):

    # Om s inte innehåller några element, returneras 0. Annars returneras
    # kvoten av summan och längden av s.
    if len(s) == 0:
        return 0
    else:
        return sum(s) / len(s)

# En lista och en tupel skapas båda med heltal från användarens input, separerade med kommatecken.
Lista = [int(x) for x in input("Ange heltal till en lista (separerade med kommatecken): ").split(",")]
Tupel = (int(x) for x in input("Ange heltal till en tupel (separerade med kommatecken): ").split(','))

# Funktionen kallas och medelvärdet avrundas till 3 decimaler och skrivs sedan ut,
# både för listan och för tupeln.
print("Medelvärdet av listan är:", round(medelvärde(Lista),3))
print("Medelvärdet av tupeln är:", round(medelvärde(list(Tupel)),3))