a,b=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
c=0
for i in set(n):
    if m.count(i):
        c+=1
for j in set(m):
    if n.count(j):
        c+=1
print(c//2)