hrow=int(input())
for i in range(hrow,0,-1):
    for j in range(1,i):
        print(' ',end="")
    for k in range(0,hrow):
        if(i==1 or i==hrow or k==0 or k==hrow-1):
            print('*',end="")
        else:
            print(' ',end="")
    print()