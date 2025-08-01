# Användaren anger ett tal x.
x=float(input("Ange x: "))

def Newtons_metod(x):
    
    gissning = x / 2  # Startgissning
    
    # Medan loopen inte bryts (vilket den gör då skillnaden mellan gissningen och den nya
    # gissningen är tillräckligt liten), används Newtons metod för att komma allt närmare
    # kvadratroten ur x.
    while True:
        ny_gissning = (gissning + x / gissning) / 2
        if abs(ny_gissning - gissning) < 0.000001:
            break
        gissning = ny_gissning
    
    # Gissningen returneras.
    return gissning
 
# Om talet är negativt skrivs ett felmeddelande ut.
if x < 0:
    print("Kan inte beräkna roten ur negativa tal.")

# Annars kallas funktionen och resultatet skrivs ut.
else:
    print("Roten av x är circa: ", Newtons_metod(x),)