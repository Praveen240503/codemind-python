a,b=map(int,input().split())
m=list(map(int,input().split()))
n=list(map(int,input().split()))
c=0
k=[]
for i in sorted(set(m),key=m.index):
    for j in set(n):
        if i==j:
            k.append(i)
for f in k:
    print(f,end=' ')