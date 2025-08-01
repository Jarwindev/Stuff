n=int(input("Ange ett heltal (större än 0): "))

def primtal(n):
    j=0
    if n==1:
        j+=1
    for i in range(1,n):
        if n%i == 0:
            j+=1
    if j==1:
        return True
    else:
        return False           

if n>0:
    bool=primtal(n)
    if bool:
        print("Talet är ett primtal.")
    else:
        print("Talet är inte ett primtal.")
else:
    print("Talet måste vara större än 0!")