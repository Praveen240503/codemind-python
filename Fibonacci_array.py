n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(2,n):
    if a[i-1]+a[i-2]==a[i]:
        c=1
    else:
        c=0
        break
if c==1:
    print('yes')
else:
    print('no')