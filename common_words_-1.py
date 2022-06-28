x = list(map(str,input().lower().split()))
y = list(map(str,input().lower().split()))
c=0
for i in x:
    if y.count(i)==1:
        c+=1
print(c)