a=int(input())
x=list(map(int,input().split()))
s,t=map(int,input().split())
c=0
for i in x:
    if i>=s and i<=t:
        c+=i
print(c)