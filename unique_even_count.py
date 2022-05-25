n=int(input())
a=list(map(int,input().split()))
x=set(a)
c=0
for i in x:
    if i%2==0:
        c+=1
print(c)