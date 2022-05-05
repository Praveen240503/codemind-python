x=int(input())
a,b=0,1
if x==0:
    print(True)
c=a+b
while c<x:
    c=a+b
    a=b
    b=c
if x==c:
    print(True)
else:
    print(False)