# Program som beräknar betyg baserat på poäng.

# Användaren anger antalet poäng, 

p=int(input("Hur många poäng fick du?"))

# och programmet beräknar betyget enligt en given skala.
# Betyget skrivs sedan ut.

if(p<25):
    print("Betyg: F")
elif(25<=p<30):
    print("Betyg: E")
elif(30<=p<35):
    print("Betyg: D")
elif(35<=p<40):
    print("Betyg: C")
elif(40<=p<45):
    print("Betyg: B")
elif(45<=p<=50):
    print("Betyg: A")

# Om användaren anger fler än 50 poäng, skrivs ut att det är ogiltigt.

else:
    print('Högst 50 poäng möjliga!')
