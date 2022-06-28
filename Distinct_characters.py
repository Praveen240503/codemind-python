x = input()
for i in sorted(set(x)):
    if i>='a' and i<='z':
        if x.count(i)==1:
            print(i,end="")
