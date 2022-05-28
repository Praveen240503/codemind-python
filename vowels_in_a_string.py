n=input()
a=input()
c=[]
for i in range(len(n)):
    if n[i]==a:
        print(True)
        print(i)
        break
else:
    print(False)