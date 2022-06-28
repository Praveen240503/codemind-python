l=list(map(str,input().split()))
for i in l:
    n = ord(min(i))
    m = ord(max(i))
    print(m-n,end=" ")