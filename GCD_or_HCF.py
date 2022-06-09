x , y = map(int,input().split())
l=[]
m=[]
h=[]
for i in range(1,x+1):
    if x%i==0:
        l.append(i)
for j in range(1,y+1):
    if y%j==0:
        m.append(j)
for k in l:
    for n in m:
        if k==n:
           h.append(k)
if h!=0:
    print(max(h))
else:
    print('-1')