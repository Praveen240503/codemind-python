a,b=map(int,input().split())
s=0
for i in range(a):
    n=list(map(int,input().split()))
    for j in range(len(n)):
        if i!=0 and i!=(a-1):
            if j!=0 and j!=len(n)-1:
                s+=n[j]
print(s)