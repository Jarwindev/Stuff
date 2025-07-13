Sek=int(input("Hur många sekunder har gått?"))
if(Sek<0):
    Sek=abs(Sek)
    Min=Sek//60
    Tim=Sek//3600
    Min=(Min-(Tim*60))
    Sek=(Sek-(Min*60+Tim*3600))
    print("Det har gått", -Tim, "timmar,", Min, "minuter och", Sek, "sekunder.")
else:
    Min=Sek//60
    Tim=Sek//3600
    Min=(Min-(Tim*60))
    Sek=(Sek-(Min*60+Tim*3600))
    print("Det har gått", Tim, "timmar,", Min, "minuter och", Sek, "sekunder.")

#Programmet konverterar sekunder till timmar, minuter och sekunder.