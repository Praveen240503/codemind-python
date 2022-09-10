import math
def fun(n):
    root=math.sqrt(n)
    if(int(root)**2==n):
        return True
    else:
        return False
n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    if(fun(i)):
        s=s+i
print(s)