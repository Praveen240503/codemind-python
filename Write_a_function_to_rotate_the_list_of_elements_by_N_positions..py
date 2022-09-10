n=int(input())
arr=list(map(int,input().split()))
k=int(input())
if k>n:
    k=int(k%len(arr))
arr=(arr[-k:]+ arr[:-k])
print(' '.join([str(i) for i in arr]))