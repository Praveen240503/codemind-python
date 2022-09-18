a=int(input())
x=list(map(int,input().split()))
s,t=map(int,input().split())
c=[]
for i in x:
    if i>=s and i<=t:
        c.append(i)
print(sum(c))