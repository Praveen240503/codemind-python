s=input()
a=input()
i=0
c=0
while i<len(s):
    if(s[i]==a):
        c+=1
    i+=1
if(c==0):
    print('-1')
else:
    print(c)