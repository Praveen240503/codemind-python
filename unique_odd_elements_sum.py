x=int(input())
a=list(map(int,input().split()))
n=set(a)
c=0
for i in n:
    if i%2!=0:
        c+=i
print(c)