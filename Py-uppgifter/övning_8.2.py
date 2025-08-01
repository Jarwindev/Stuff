n=int((input("Ange ett heltal: ")))

def multipler(n):
    if n<=0 or n>10:
        print("Talet n måste vara mellan 1 och 10!")
    else:
        for i in range(1,11):
            print(i, i*n)
        
multipler(n)