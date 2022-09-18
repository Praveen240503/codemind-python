def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=0
for i in range(a):
    if prime(b[i]) and b[i]<=c:
        d+=1
print(d)