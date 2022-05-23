n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
l=[]
for i in range(0,n):
    if a[i]>=x and a[i]<=y:
        pass
    else:
        l.append(a[i])
if len(l)!=0:
    print(max(l))
else:
    print('-1')