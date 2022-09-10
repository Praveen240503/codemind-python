l=list(map(int,input().split(",")))
s=[]
k=[]
for i in l:
    for j in range(1,i+1):
        if i%j==0:
            s.append(j)
    if sum(s) in l:
        k.append(i)
        s.clear()
    else:
        s.clear()
k.sort()
if len(k)>0:
    print(*k)
else:
    print(-1)