x = int(input())
y = list(map(int,input().split()))
l=[]
for i in y:
    m = i**2
    l.append(m)
l = sorted(l)
for j in l:
    print(j,end=" ")