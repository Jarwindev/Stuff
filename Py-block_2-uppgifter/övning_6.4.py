Lista=[]
Värden=input("Ange uppmätta värden, separerade med kommatecken: ")
Lista=Värden.split(",")
while(len(Lista) > 2):
    Lista.remove(max(Lista))
    Lista.remove(min(Lista))
if len(Lista) == 2:
    print("Medianvärdet är:", (float(Lista[0]) + float(Lista[1])) / 2)
else:
    print("Medianvärdet är:", Lista[0])