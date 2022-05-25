def dig(n):
    v=0
    while n!=0:
        x=n%10
        v+=x
        n//=10
    return v
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    a=dig(i)
    c+=a
print(c)