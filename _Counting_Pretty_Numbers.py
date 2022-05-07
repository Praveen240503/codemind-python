x=int(input())
c=0
for i in range(x):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        s=j%10
        if s==2 or s==3 or s==9:
            c+=1
    print(c)
    c=0
    