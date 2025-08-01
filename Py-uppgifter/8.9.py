# Program som tar in en lista med heltal och skapar en ny lista med endast udda tal
# Använder filter och ett lambda-uttryck för att skapa den nya listan

# Användare anger en lista med heltal
Lista=input("Ange heltal till en lista (separerade med kommatecken): ").split(",")

# Filtrerar listan för att endast behålla udda tal
# Använder en lambda-funktion som returnerar True för udda tal
Ny_lista = filter(lambda x: int(x) % 2 != 0, Lista)

# Konverterar den filtrerade listan till en vanlig lista och skriver ut den
print("Listan med udda tal:", list(Ny_lista))
