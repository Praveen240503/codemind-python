n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
c=0
for i in range(0,n):
    if a[i]>=x and a[i]<=y:
        pass
    else:
        c+=a[i]
print(c)