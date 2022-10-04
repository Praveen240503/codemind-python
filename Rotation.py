for i in range(int(input())):
    n,k=input().split()
    n=int(n)
    arr=list(map(int,input().split()))
    k=int(k)
    if k>n:
        k=int(k%len(arr))
    arr=(arr[-k:]+arr[:-k])
    print(' '.join([str(i) for i in arr]))