a=int(input("2nd degree coefficient?" ))
b=int(input("1st degree coefficient?" ))
c=int(input("Constant?" ))
rm=float(input("Range multiplier? (Type 1 to bypass) "))
ru=int(input("Upper range limit? "))
rl=int(input("Lower range limit? (Must be smaller than than the upper limit) "))
for x in range(rl, ru+1):
    y=(a*x**2-b*x+c)
    x=x*rm
    y=round(y,3)
    print(y, end=", ")