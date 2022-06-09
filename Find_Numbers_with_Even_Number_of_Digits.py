x = int(input())
y = list(map(int,input().split()))
f = 0
for i in y:
    if len(str(i))%2==0:
        f+=1
print(f)