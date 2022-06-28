x = list(map(str,input().split()))
b=[]
c=[]
for i in x:
    n = max(i)
    b.append(n)
    m = min(i)
    b.append(m)
    for j in i:
        c.append(j)
a = min(b)
d = max(b)
print(a,end=" ")
print(c.count(a),end=" ")
print(d,end=" ")
print(c.count(d),end=" ")