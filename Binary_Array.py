n=int(input())
a=list(map(int,input().split()))
k=len(a)
c=0
for i in a:
    if i==0 or i==1:
        c+=1
if c==k:
    print(True)
else:
    print(False)