n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(n):
    if a[i]%2!=0:
        l.append(i)
e=a[max(l)]
print(e)