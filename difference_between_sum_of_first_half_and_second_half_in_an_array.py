n=int(input())
a=list(map(int,input().split()))
x,y=0,0
for i in range(0,n//2):
    x+=a[i]
for j in range(n//2,n):
    y+=a[j]
print(abs(x-y))