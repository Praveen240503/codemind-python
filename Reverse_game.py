def rev(n):
    v=0
    s=n
    while n!=0:
        x=n%10
        v=v*10+x
        n//=10
    return v
n=int(input())
a=list(map(int,input().split()))
for i in a:
    print(rev(i),end=" ")