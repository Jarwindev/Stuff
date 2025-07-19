Italien=set(input("Ange färgerna i den Italiens flagga, separerade med kommatecken: ").split(","))
Spanien=set(input("Ange färgerna i den Spaniens flagga, separerade med kommatecken: ").split(","))
Frankrike=set(input("Ange färgerna i den Frankrikes flagga, separerade med kommatecken: ").split(","))
Portugal=set(input("Ange färgerna i den Portugals flagga, separerade med kommatecken: ").split(","))
Lista=[Italien, Spanien, Frankrike, Portugal]

print("Färgerna i Italiens flagga är:", Italien)
print("Färgerna i Spaniens flagga är:", Spanien)
print("Färgerna i Frankrikes flagga är:", Frankrike)
print("Färgerna i Portugals flagga är:", Portugal) 
print("Färgerna i flaggorna är:", set.union(*Lista))
print("Färgerna som är lika i alla flaggor är:", set.intersection(*Lista))
