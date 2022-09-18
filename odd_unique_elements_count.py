a=int(input())
b=list(map(int,input().split()))
c=set(b)
d=0
for i in c:
    if i%2!=0:
        d+=1
print(d)