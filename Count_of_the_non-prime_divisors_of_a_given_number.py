def prime(n):
    if n==1:
        return 0
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    else:
        return 1

a = int(input())
c=[]
for i in range(1,a+1):
    if a%i==0:
        if prime(i):
            pass
        else:
            c.append(i)
print(len(c))