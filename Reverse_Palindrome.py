def palin(n):
    v=0
    s=n
    while n!=0:
        x=n%10
        v=v*10+x
        n//=10
    d=s+v
    e=str(d)
    if str(d)==e[::-1]:
        print(d)
    else:
        palin(d)
        
        
a=int(input())
palin(a)