n=input()
c=[]
for i in n:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        c.append(i)
if c==[]:
    print('0')
else:
    print(len(c))