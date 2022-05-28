n=input()
k=[]
for i in n:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        k.append(i)
k=sorted(set(k),key=k.index)
if k==[]:
     print('-1')
else:
    for j in k:
        print(j,end=' ')