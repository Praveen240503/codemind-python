n=int(input())
for i in range(n):
    for j in range(n):
        if i==j:
            print('0',end='')
        else:
            print('x',end='')
    print()