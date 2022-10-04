n,k=map(int,input().split())
s,c=0,0
l=list(map(int,input().split()))
for i in l:
    if i<=k:
        c+=1
    elif i>k and s==0:
        s+=1
        continue
    else:
        break
print(c)