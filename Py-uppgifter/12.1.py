# Kod som låter användaren mata in färgerna i flaggorna för Italien, Spanien, Frankrike och Portugal.
# Använder mängder för att hantera färgerna och jämföra dem mellan flaggorna.

Italien=set(input("Ange färgerna i den Italiens flagga, separerade med kommatecken: ").split(","))
Spanien=set(input("Ange färgerna i den Spaniens flagga, separerade med kommatecken: ").split(","))
Frankrike=set(input("Ange färgerna i den Frankrikes flagga, separerade med kommatecken: ").split(","))
Portugal=set(input("Ange färgerna i den Portugals flagga, separerade med kommatecken: ").split(","))

# Skapar en lista med flaggornas färger för att kunna använda mängdoperationer.

Lista=[Italien, Spanien, Frankrike, Portugal]

# Skriver ut färgerna i varje flagga, unionen av alla färger och snittet av färgerna i alla flaggor.

print("Färgerna i Italiens flagga är:", Italien)
print("Färgerna i Spaniens flagga är:", Spanien)
print("Färgerna i Frankrikes flagga är:", Frankrike)
print("Färgerna i Portugals flagga är:", Portugal) 
print("Färgerna i flaggorna är:", set.union(*Lista))
print("Färgerna som är lika i alla flaggor är:", set.intersection(*Lista))
