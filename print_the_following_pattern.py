n=int(input())
a,b=1,1
for i in range(n):
    for j in range(n-1,i,-1):
        print(" ",end='')
    for j in range(1,a+1):
        print(abs(j-b),end="")
    print()
    a+=2
    b+=1