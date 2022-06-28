x = int(input())
for i in range(x):
    a = int(input())
    l = sorted(list(map(int,input().split())))
    n = len(l)//2
    m = len(l)
    s=[]
    if m%2==1:
        for j in range(n):
            s.append(l[m-(j+1)])
            s.append(l[j])
        s.append(l[n])
        print(*s)
    else:
        for j in range(n):
            s.append(l[m-(j+1)])
            s.append(l[j])
        print(*s)