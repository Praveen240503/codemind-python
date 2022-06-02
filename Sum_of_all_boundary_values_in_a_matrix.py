a,b=map(int,input().split())
s=0
for i in range(a):
    n=list(map(int,input().split()))
    for j in range(len(n)):
        if i==0 or i==a-1:
                s+=n[j]
        else:
            if j==0 or j==len(n)-1:
                s+=n[j]
print(s)