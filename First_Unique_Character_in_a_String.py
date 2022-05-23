n=input()
c=0
for i in range(len(n)):
    for j in range(len(n)):
        if n[i]==n[j]:
            c+=1
    if c==1:
        print(i)
        break
    c=0
else:
    print('-1')