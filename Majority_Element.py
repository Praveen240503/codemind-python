x = int(input())
l = list(map(int,input().split()))
n=[]
c=0
for i in list(set(l)):
    for j in l:
        if i==j:
            c+=1
    n.append([c,i])
    c=0
m=max(n)
print(m[1])