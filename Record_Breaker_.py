cases = int(input().strip())
for q in range(1, cases + 1):
    l = int(input().strip())
    ls = list(map(int, input().split(" ")))
    l = len(ls)
    local_max = 0
    count = 0
    for i in range(l):
        if i == 0:
            if ls[1] < ls[0]:
                local_max = ls[0]
                count += 1
            continue
        if i == l - 1:
            if ls[i] > ls[i - 1] and ls[i] > local_max:
                count += 1
            break
        if ls[i] > ls[i - 1] and ls[i] > ls[i + 1] and ls[i] > local_max:
            count += 1
            local_max = ls[i]
            continue
    
    print("Case #{}: {}".format(q, count))