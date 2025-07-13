a=int(input("2nd degree coefficient?" ))
b=int(input("1st degree coefficient?" ))
c=int(input("Constant?" ))
r=float(input("Range multiplier? "))
for x in range(-10, 11):
    y=(a*x**2-b*x+c)
    x=x*r
    y=round(y,3)
    print(y, end=", ")