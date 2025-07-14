PN=input("Ange ett personnummer: ")
if int(PN[len(PN)-2:]) % 2== 0:
    print("Personen är kvinna.")
else:
    print("Personen är en man.")