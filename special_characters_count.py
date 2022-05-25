n=input()
c=0
for i in n:
    if i>='a'and i<='z'or i>='A' and i<='Z'or i==' ':
        pass
    else:
        c+=1
print(c)