x,y = map(int,input().split())
if(x+1==y or x-1==y):
    print("Yes")
elif(x== 10 and y==1):
    print("Yes")
elif(x==1 and y==10):
    print("Yes")
else:
    print("No")