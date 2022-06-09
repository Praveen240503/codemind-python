x , y = map(int,input().split())
l = len(str(x))
v = x%(10**y)
while x!=0:
    b = x%(10**(l-y))
    x = x//(10**(l-y))
print(abs(b-v))