def prime(n):
    if n==1:
        return 0
    for i in range(2,(int(n**0.5)+1)):
        if n%i==0:
            return 0
    return 1
a=int(input())
b=a+1
while True:
    if prime(b):
        n=str(b)
        x=n[::-1]
        if x==n:
            if prime(int(x)):
                print(x)
                break
    b+=1