n,k=input().split()
n=int(n)
matrix=[]
for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
res=[max(idx) for idx in zip(*matrix)]
for i in res:
    print(i)