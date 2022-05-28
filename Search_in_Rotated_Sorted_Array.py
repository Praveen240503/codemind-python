n=int(input())
a=list(map(int,input().split()))
c=int(input())
flag=0
for i in a:
    if i==c:
        print(a.index(i))
        flag=0
        break
    else:
        flag=1
if flag==1:
    print('-1')