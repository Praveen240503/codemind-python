x = input()
c=0
for i in x:
    if i>='a' and i<='z':
        if x.count(i)==1:
            c+=1
print(c)