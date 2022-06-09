x = int(input())
l = list(map(int,input().split()))
y = int(input())
m = max(l)
lk = []
for i in l:
    if (y+i)>=m:
        print("True",end=" ")
    else:
        print('False',end=" ")