MAX=100
def printDiagonalSums(math,n):
    principal=0
    secondary=0
    for i in range(0,n):
        for j in range(0,n):
            if(i==j):
                principal+=matrix[i][j]
            if((i+j)==(n-1)):
                secondary+=matrix[i][j]
    print("Principal Diagonal:%d"%principal)
    print("Secondary Diagonal:%d"%secondary)
n=int(input())
matrix=[]
for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
printDiagonalSums(matrix,n)