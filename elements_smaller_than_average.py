n=int(input())
a=list(map(int,input().split()))
avg=0
c=0
for i in range(len(a)):
    avg+=a[i]
    x=avg//n
for i in a:
    if i<=x:
        c+=1
print(c)