x = list(map(str,input().split()))
a = len(x)
x = x[a-1]
n = min(x)
m = n.lower()
if x.count(m)!=0:
    print(m)
else:
    print(n)