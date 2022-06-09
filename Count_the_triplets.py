x = int(input())
for i in range(x):
    n = int(input())
    c=0
    m = list(map(int,input().split()))
    for j in range(len(m)):
        for k in range(len(m)):
            if m[j]!=m[k]:
                if m[j]+m[k] in m:
                    c+=1
    if c==0:
        print('-1')
    elif c!=0:
        print(c//2)