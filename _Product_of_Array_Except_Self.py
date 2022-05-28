n=int(input())
a=list(map(int,input().split()))
c=1
for i in range(len(a)):
    for j in range(len(a)):
        if j==i:
            pass
        else:
            c*=a[j]
    print(c,end=' ')
    c=1