a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(0,len(b)-1):
    if b[i]<b[i+1]:
        c+=1
if c==len(b)-1:
    print('yes')
else:
    print('no')