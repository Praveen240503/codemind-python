x = int(input())
l = list(map(int, input().split()))
if x % 2 == 1:
    for i in range(x//2+1):
        if i!=(x-1)-i:
            print(l[i],end=" ")
            print(l[(x-1)-i],end=" ")
    print(l[i],end=" ")
    print('0')
elif x%2==0:
    for i in range(x//2):
        if i != (x-1) - i:
            print(l[i], end=" ")
            print(l[(x-1) - i], end=" ")