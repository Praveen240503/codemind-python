l = list(map(str,input().split()))
s=0
c=0
for i in l:
    n = max(i)
    s+=ord(n)
    m=min(i)
    c+=ord(m)
print(s-c)