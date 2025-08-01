# Användaren anger 2 heltal.
i=int(input("Ange ett heltal (större än 0): "))
j=int(input("Ange ett annat heltal (större än 0): "))

def relativa_primtal(i,j):
 
    # 2 listor skapas, för att hålla talen i och j´s delare.
    i_delare_lista=[]
    j_delare_lista=[]

    # Specialfall där i eller j eller lika med 1, då vet vi att de är relativa primtal.
    if i==1 or j==1:
        return True
    
    # Annars körs 2 for-loopar som kollar alla tal mellan 2 och i, och mellan 2 och j.
    # Om ett tal visar sig vara en jämn delare, adderas den till listan med talets delare 
    # genom metoden append.
    else:
        for tal in range(2,i):
            if i%tal==0:
                i_delare_lista.append(tal)

        for tal in range(2,j):
            if j%tal==0:
                j_delare_lista.append(tal)

    # 2 mängder skapas av de 2 listorna, detta för att kunna använda snittmängd.
    # Listorna behövdes för att kunna använda metoden append.
    i_delare=set(i_delare_lista)            
    j_delare=set(j_delare_lista)

    # Om längden av snittmängden är 0 (om i och j inte har några gemensamma delare utom 1),
    # så returneras true, annars false.

    if len(j_delare&i_delare)==0:
        return True
    
    else:
        return False 
              
#Om i och j båda är positiva, fortsätter programmet,
if i>0 and j>0:
 
    # Om i och j är samma tal, skrivs ett felmeddelande ut.
    if i==j:
        print("Talen måste vara olika!")

    # Annars kallas funktionen, och användaren får reda på om talen i och j är relativa primtal.
    else:
        if relativa_primtal(i,j):
            print("Talen är relativa primtal.")

        else:
            print("Talen är inte relativa primtal.")

# annars skrivs ett felmeddelande ut.
else:
    print("Båda talen måste vara större än 0!")