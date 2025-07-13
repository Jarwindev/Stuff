c=1
n=0
ans=0
while(c<1000):
    n=1/c-(1/(c+1)) 
    c=c+2
    ans=ans+n
    print(ans)