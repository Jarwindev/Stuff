# Program som beräknar medianvärdet av en lista med uppmätta värden.

# Användaren matar in en lista med värden separerade av kommatecken.

Lista=[]
Värden=input("Ange uppmätta värden, separerade med kommatecken: ")
Lista=Värden.split(",")

# Medan listan har fler än två element, tas det största och minsta värdet bort.
# Detta fortsätter tills endast två eller ett värde återstår.

while(len(Lista) > 2):
    Lista.remove(max(Lista))
    Lista.remove(min(Lista))

# Om det finns två värden kvar, beräknas medianvärdet som medelvärdet av dessa.
# Om det finns ett värde kvar, är det medianvärdet.

if len(Lista) == 2:
    print("Medianvärdet är:", (float(Lista[0]) + float(Lista[1])) / 2)
else:
    print("Medianvärdet är:", Lista[0])