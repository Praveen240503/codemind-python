n=int(input())
a=list(map(int,input().split()))
c=list(set(a))
s=0
g=0
for i in c:
    for j in a:
        if i==j:
            s+=1
    g+=s//2
    s=0
print(g)