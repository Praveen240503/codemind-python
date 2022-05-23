def is_fib(j):
    a = 0
    b = 1
    c = a+b
    while c<j:
        c = a + b
        a = b
        b = c
    if c == j:
        return j
n = int(input())
k=n
for j in range(n,0,-1):
    if is_fib(j):
        a = j
        break
while k!=0:
    if is_fib(k):
        b = k
        break
    k+=1
if (n-a)<(b-n):
    print(a)
elif (n-a)==(b-n):
    print(a,b)
else:
    print(b)