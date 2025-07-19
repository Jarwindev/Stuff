# Program som konverterar ett datum från svenskt format till amerikanskt format.

# Användaren anger ett datum i formatet DD-MM-YY.

Datum_SE=input("Ange ett datum i svenskt format: ")

# Konverterar datumet till amerikanskt format MM/DD/YY.
# Datumet delas upp i delar och omordnas.

Datum_US=Datum_SE[5:7] + "/" + Datum_SE[8:10] + "/" + Datum_SE[2:4]

# Skriver ut det konverterade datumet.

print("Datum i amerikanskt format:", Datum_US)
