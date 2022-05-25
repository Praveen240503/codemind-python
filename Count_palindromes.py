def palin(n):
    v=0
    s=n
    while n!=0:
        x=n%10
        v=v*10+x
        n=n//10
    if v==s:
        return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if palin(i):
        c+=1
print(c)