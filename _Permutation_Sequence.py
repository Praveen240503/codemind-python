from itertools import permutations
x , y =map(int,input().split())
l = list(permutations(range(1,x+1)))
for i in l[y-1]:
    print(i,end="")