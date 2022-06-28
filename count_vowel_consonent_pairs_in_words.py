x = list(map(str,input().split()))
l = ['a','e','i','o','u','A','E','I','O','U']
c=0
for i in x:
    for j in range(0,len(i)//2):
        if (i[j] in l) and (i[len(i)-j-1] not in l) or (i[j] not in l) and (i[len(i)-j-1] in l):
            c+=1
print(c)