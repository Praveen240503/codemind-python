n,k,m=map(int,input().split())
l=list(map(int,input().split()))
s=l[-k:]+l[:-k]
for i in range(m):
    print(s[int(input())])