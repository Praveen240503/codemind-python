n=int(input())
for i in range(n):
    p=int(input())
    a=list(map(int,input().split()))
    for i in range(1,p+1):
        if(i not in a):
            print(i)