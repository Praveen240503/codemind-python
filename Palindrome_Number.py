t=int(input())
while t:
    i = int(input())
    rev=0
    temp=i
    while temp:
        rev=rev*10+temp%10
        temp//=10
    if rev==i:
        print(True)
    else:
        print(False)
    t-=1