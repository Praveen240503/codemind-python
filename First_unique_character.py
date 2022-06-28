x = input()
c=0
for i in sorted(set(x),key=x.index):
    if x.count(i)==1:
        print(i)
        c=1
        break
if c==0:
    print('-1')