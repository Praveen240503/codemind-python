x=int(input())
l = list(map(int,input().split()))
c,d=0,0
for i in range(len(l)):
    if i%2==0:
        c+=l[i]
    else:
        d+=l[i]
print(abs(c-d))