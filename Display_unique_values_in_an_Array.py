n=int(input())
a=list(map(int,input().split()))
s=list(set(a))
k=[]
c=0
for i in s:
    for j in a:
        if i==j:
            c+=1
    if c==1:
        k.append(i)
    c=0
if k==[]:
    print('-1')
else:
    for d in k:
        print(d,end=' ')
    