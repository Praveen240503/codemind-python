n=int(input())
c=0
while n:
    s=input()
    if s[1]=='+':
        c+=1
    else:
        c-=1
    n-=1
print(c)