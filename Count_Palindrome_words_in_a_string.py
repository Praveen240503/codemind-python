x = list(map(str,input().split()))
c=0
for i in x:
    m=i.lower()
    n = m[::-1]
    if n==m:
        c+=1
print(c)