a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
for i in c:
    if i not in d:
        print(i,end=' ')
for j in d:
    if j not in c:
        print(j,end=' ')