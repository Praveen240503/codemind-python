class Solution:
    def createTargetArray(self,nums,index):
        l,ans=len(nums),[]
        for i in range(l):ans.insert(index[i],nums[i])
        return ans
ob=Solution()
c1=int(input())
nums=list(map(int,input().split()))
c2=int(input())
index=list(map(int,input().split()))
k=ob.createTargetArray(nums,index)
print(' '.join([str(i) for i in k]))