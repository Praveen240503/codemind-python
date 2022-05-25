def dig(n):
    v=0
    while n!=0:
        x=n%10
        v+=1
        n//=10
    return v
n=int(input())
a=list(map(int,input().split()))
x=0
e=0
c=[]
for i in a:
    x=dig(i)
    c.append(x)
d=max(c)
for j in c:
    if d==j:
        e+=1
print(e)