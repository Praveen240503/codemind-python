n=int(input())
a=list(map(int,input().split()))
for i in a:
    if a.count(i)==2:
        print(i)
        break