n=int(input())
a=0
r=n**2
while n!=0:
    f=n%10
    a=a*10+f
    n=n//10
s=a**2
u=0
while s!=0:
    g=s%10
    u=u*10+g
    s=s//10
if(u == r):
    print(True)
else:
    print(False)