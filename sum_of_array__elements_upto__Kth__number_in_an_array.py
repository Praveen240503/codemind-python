n=int(input())
a=list(map(int,input().split()))
x=int(input())
s=a.index(x)
c=0
for i in a:
    c+=i
    if i==x:
        break
print(c)