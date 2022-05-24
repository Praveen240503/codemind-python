x=int(input())
a=list(map(int,input().split()))
for i in sorted(set(a),key=a.index):
    print(i,end=" ")
    n=a.count(i)
    print(n,end=" ")