a=int(input())
d=0
for i in range(a):
    n=input()
    c=len(n)
    for j in n:
        if j>='0' and j<='9':
            d+=1
    if c==d:
        print(True)
    else:
        print(False)
    d=0