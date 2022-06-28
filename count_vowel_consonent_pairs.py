x = input()
l = ['a','e','i','o','u','A','E','I','O','U']
a = [" "]
c=0
for i in range(0,len(x)//2):
    if ((x[i] in l) and (x[len(x)-i-1] not in l)) or ((x[i] not in l) and (x[len(x)-i-1] in l)):
        c+=1
    if (x[i]==" " and x[len(x)-i-1]!=" "):
        c-=1
print(c)