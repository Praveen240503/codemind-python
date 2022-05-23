n=int(input())
a=list(map(int,input().split()))
l=[]
m=[]
for i in range(n):
    if a[i]%2==0:
        l.append(a[i])
    else:
        m.append(a[i])
for i in l:
    print(i,end=' ')
for i in m:
    print(i,end=' ')
    