n=int(input())
c=0
a=[]
for i in range(n):
    a.append(int(input()))
p=int(input())
for i in a:
    if(i<=p):
        c=c+1
    else:
        c=c+2
print(c)