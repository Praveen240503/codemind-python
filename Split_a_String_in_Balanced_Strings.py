n=input()
c=0
x=0
for i in n:
    if i=='R':
        c+=1
    if i=='L':
        c-=1
    if c==0:
        x+=1
print(x)