x,y=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(0,x):
    if a[i]%y==0:
        c+=1
print(c)