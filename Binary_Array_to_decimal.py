x = int(input())
l = list(map(int,input().split()))
j=0
v=0
for i in range(x-1,-1,-1):
    v+=(l[i]*(2**j))
    j+=1
print(v)