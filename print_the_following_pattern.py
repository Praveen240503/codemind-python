n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(i+64),end=' ')
    print()