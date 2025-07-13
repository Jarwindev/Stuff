y=(int(input("Precision? (Number of decimals for approximation.) ")))
c=1
n=0
ans=0
x=0.1**y
while(abs(1/c)>=x):
    n=1/c-(1/(c+1)) 
    c=c+2
    ans=ans+n
    n=0
print(ans)
     
#Resource intensive, use with care for y>8.