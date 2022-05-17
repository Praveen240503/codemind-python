n=int(input())
a=list(map(int,input().split()))
f=0
for i in range (0,n):
    f=f*10+a[i]
f+=1
s=str(f)
for i in s:
    print(i,end=' ')