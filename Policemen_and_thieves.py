def solve(lis,k):
    Po=[x for x in range(len(lis)) if lis[x]=='P']
    Th=[x for x in range(len(lis)) if lis[x]=='T']
    i,j=0,0
    ans=0
    while i<len(Po) and j<len(Th):
        if max(Po[i],Th[j])-min(Po[i],Th[j])<=k:i+=1;j+=1;ans+=1
        elif Po[i]>Th[j]:j+=1
        else:i+=1
    return ans
for _ in range(int(input())):
    n,k=map(int,input().split())
    ans=0
    for i in range(n):
        ans+=(solve(list(map(str,input().split())),k))
    print(ans)