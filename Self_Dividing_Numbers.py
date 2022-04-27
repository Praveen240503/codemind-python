def self_dividing(n):
    for d in str(n):
        if d=='0' or n % int(d)>0:
            return False
    return True
left=int(input())
right=int(input())
for n in range(left,right+1):
    if self_dividing(n):
        print(n,end=' ')