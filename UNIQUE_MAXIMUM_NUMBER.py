x = int(input())
b = list(map(int,input().split()))
c=0
l=[]
for i in range(len(b)):
    for j in range(len(b)):
        if b[i]==b[j]:
            c+=1
    if c==1:
        l.append(b[i])
    c=0
if len(l)==0:
    print('-1')
elif l!=0:
    print(max(l))