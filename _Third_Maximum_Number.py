n = int(input())
y = list(map(int,input().split()))
m = sorted(list(set(y)))
print(m[len(m)-3])