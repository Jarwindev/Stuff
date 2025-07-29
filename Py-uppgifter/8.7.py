def medelvärde(s):
    if len(s) == 0:
        return 0
    return sum(s) / len(s)
Lista = [int(x) for x in input("Ange heltal till en lista (separerade med kommatecken): ").split(",")]
Tupel = (int(x) for x in input("Ange heltal till en tupel (separerade med kommatecken): ").split(','))
print("Medelvärdet av listan är:", round(medelvärde(Lista),3))
print("Medelvärdet av tupeln är:", round(medelvärde(list(Tupel)),3))