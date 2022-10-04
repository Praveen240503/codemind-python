class Solution:
    def canBeEqual(self,target,arr):
        for i in arr:
            if i in target:
                target.remove(i)
        if len(target)>0:
            return False
        else:
            return True
ob=Solution()
cl=int(input())
target=list(map(int,input().split()))
c2=int(input())
arr=list(map(int,input().split()))
k=ob.canBeEqual(target,arr)
print(k)