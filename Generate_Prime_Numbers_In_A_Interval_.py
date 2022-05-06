def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
x=int(input())
y=int(input())
for i in range(x,y+1):
    if prime(i):
        print(i)