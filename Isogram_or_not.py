x = input()
c=0
for i in x:
    if x.count(i)==1:
        c+=1
if c==len(x):
    print(True)
else:
    print(False)