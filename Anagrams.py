s = input()
t = input()
t = t.lower()
t = list(t)
s = s.lower()
c=0
for i in s:
    if t.count(i)==1:
        c+=1
if c==len(s):
    print(True)
else:
    print(False)