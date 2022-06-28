def is_prime(j):
    i=2
    v=0
    while i!=j:
        if j%i==0:
            v=1
        i+=1
    if v==0:
        return j
y = int(input())
b=y
for j in range(y,2,-1):
    if is_prime(j):
        n=j
        break
while b!=0:
    if is_prime(b):
        m=b
        break
    b+=1
if (y-n)<(m-y):
    print(abs(n-y))
elif (y-n)==(m-y):
    print(abs(n-y))
else:
    print(abs(m-y))