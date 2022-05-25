a=int(input())
x=list(map(int,input().split()))
s,t=map(int,input().split())
c=[]
h=[]
for i in x:
    if i>=s and i<=t:
        c.append(i)
    else:
        h.append(i)
if len(h)==0:
    print('-1')
else:
    print(min(h))