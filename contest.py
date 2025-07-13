p=0
ptotal1=0
mi=11
ma=-1
j=int(input("Amount of judges? "))
if(j<0):
    print("Exiting program...")
elif(j<3):
    print("Amount of judges needs to be at least 3!")
else:
    d=int(input("Jump difficulty? "))
    if(d<0):
        print("Exiting program...")
    else:
        for i in range(0,j):
            p=int(input("Points by judge? "))
            if(p<0):
                print("Exiting program...")
                break
            elif(p>10):
                print("Maximum points per judge: 10!")
                break
            else:
                mi=min(p,mi)
                ma=max(p,ma)
                ptotal1=ptotal1+p
                p=0
        if(i==j-1):
            pmean=(ptotal1-(mi+ma))/(j-2)
            ptotal2=pmean*3*d
            print("Final jump score=", int(ptotal2))