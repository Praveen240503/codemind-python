a,b=map(int,input().split())
s=0
for i in range(a):
    x=list(map(int,input().split()))
    for j in range(len(x)):
        if j==i or j==(len(x)-1)-i:
            s+=x[j]
print(s)