n=input()
m=['a','e','i','o','u']
c=[]
d=0
for i in n:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        c.append(i)
if len(set(c))==len(m):
    print('0')
else:
    for j in m:
        for k in c:
            if j==k:
                d+=1
        if d==0:
            print(j,end=' ')
        d=0