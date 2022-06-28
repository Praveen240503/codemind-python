x = int(input())
y = list(map(int,input().split()))
z = list(map(int,input().split()))
c=0
s,s1=0,0
for i in range(x):
    if y[i]==-1:
        c+=1
    if z[i]==-1:
        c+=1
    else:
        s+=y[i]
        s1+=z[i]
if c==2:
    print("Infinite")
else:
    c1=0
    for i in range(9999):
        if i+s==s1:
            c1+=1
    print(c1)