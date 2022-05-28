n=input()
c=[]
d=[]
for i in n:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        c.append(i)
    elif  i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        d.append(i)
a=len(set(c))
b=len(set(d))
if a==5:
    print(True)
elif b==5:
    print(True)
else:
    print(False)