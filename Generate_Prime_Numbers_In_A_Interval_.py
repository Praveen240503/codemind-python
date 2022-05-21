a = int (input())
b = int (input())
s=0
for i in range(a,b+1):
    c=0
    for j in range(2,i):
        if i%j==0:
            c=1
            break
    if c==0:
        if i!=1:
            print(i)