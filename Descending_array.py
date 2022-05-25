n=int(input())
a=list(map(int,input().split()))
b=sorted(a,reverse=True)
if a==b:
    print('yes')
else:
    print('no')