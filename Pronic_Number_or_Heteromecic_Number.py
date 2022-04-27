numb = int(input())
count = 0
for itr in range(numb):
    if itr * (itr + 1) == numb:
        count = 1
        break
if count == 1:
    print("YES")
else:
    print("NO")