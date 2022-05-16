str=input()
c=1
for i in range(1,len(str)-1):
    if str[i].isupper():
        c+=1
print(c)