x , y = map(int,input().split())
c=[]
d=[]
s=0
for i in range(x):
    l = list(map(int,input().split()))
    c.append(l)
i=0
while i!=y:
    for j in c:
        s+=j[i]
    d.append(s)
    s=0
    i+=1
print(max(d))