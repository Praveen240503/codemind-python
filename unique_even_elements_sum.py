a=int(input())
x=list(map(int,input().split()))
n=set(x)
c=0
for i in n:
    if i%2==0:
        c+=i
print(c)