x , y = map(int,input().split())
c=[]
for i in range(x):
    l = list(map(int,input().split()))
    c.append(l)
print(sum(max(c)))