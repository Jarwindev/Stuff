x=float(input("Ange x: "))

def Newtons_metod(x):
    
    if x < 0:
        raise ValueError("Kan inte beräkna roten ur negativa tal.")
    
    gissning = x / 2  # Startgissning
    
    while True:
        ny_gissning = (gissning + x / gissning) / 2
        if abs(ny_gissning - gissning) < 0.000001:
            break
        gissning = ny_gissning
    
    return gissning

print("Roten av x är circa: ", Newtons_metod(x),)

