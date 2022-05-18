n=int(input())
a=int(input())
sum=0
for i in range(n):
    h=list(map(int,input().split()))
    for j in range(a):
        sum+=h[j]
print(sum)