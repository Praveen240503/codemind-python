x = int(input())
y = list(map(int,input().split()))
z = list(map(int,input().split()))
for i in range(x):
    n = y[i]+z[i]
    print(n,end=" ")