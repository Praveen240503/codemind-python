
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or j==n-i+1:
            print(n-i+1,end=" ")
        else:
            print(" ",end="")
    print()