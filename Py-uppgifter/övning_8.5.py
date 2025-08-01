i=int(input("Ange ett heltal (större än 0): "))
j=int(input("Ange ett annat heltal (större än 0): "))

def relativa_primtal(i,j):

    i_delare_lista=[]
    j_delare_lista=[]

    if i==1 or j==1:
        return True
    
    else:
        for tal in range(2,i):
            if i%tal==0:
                i_delare_lista.append(tal)

        for tal in range(2,j):
            if j%tal==0:
                j_delare_lista.append(tal)

    i_delare=set(i_delare_lista)            
    j_delare=set(j_delare_lista)

    if len(j_delare&i_delare)==0:
        return True
    
    else:
        return False 
              

if i>0 and j>0:

    if i==j:
        print("Talen måste vara olika!")

    else:

        if relativa_primtal(i,j):
            print("Talen är relativa primtal.")

        else:
            print("Talen är inte relativa primtal.")

else:
    print("Båda talen måste vara större än 0!")
