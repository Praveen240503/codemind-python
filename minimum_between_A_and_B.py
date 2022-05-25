a=int(input())
x=list(map(int,input().split()))
s,t=map(int,input().split())
c=[]
for i in x:
    if i>=s and i<=t:
        c.append(i)
if len(c)==0:
    print('-1')
else:
    print(min(c))