n=int(input())
s=list(map(int,input().split()))
k=[]
v=len(s)
while len(s)>0:
    print(len(s))
    for i in s:
        b=min(s)
        a=i-b
        if a!=0:
            k.append(a)
    s.clear()
    s=k.copy()
    k.clear()