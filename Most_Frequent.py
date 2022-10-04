n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    z=l.count(i)
    r.append(z)
    
x=[i for i in l if l.count(i)==max(r)]
print(min(x))