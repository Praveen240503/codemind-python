x = int(input())
y = list(map(int,input().split()))
l=[]
for i in range(len(y)):
    s=0
    for j in range(len(y)):
        if y[i]>y[j]:
            s+=1
    l.append(s)
    s=0
for a in l:
    print(a,end=" ")