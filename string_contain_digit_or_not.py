n=input()
a=[]
for i in n:
    if i.isdigit():
        a.append(i)
h= len(a)
if h==0:
    print("Doesn't contain digit")
else:
    print("Contains %d digit"%h)