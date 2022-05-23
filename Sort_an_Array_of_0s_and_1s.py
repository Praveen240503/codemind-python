n=int(input())
a=list(map(int,input().split()))
for i in a:
    if i==0:
        print('0',end=' ')
for i in a:
    if i!=0:
        print(i,end=' ')