class Solution:
    def decompressRLElist(self,nums):
        decompressed=[]
        for i in range(0,len(nums)-1,2):
            decompressed=decompressed+nums[i]*[nums[i+1]]
        return decompressed
ob=Solution()
c1=int(input())
nums=list(map(int,input().split()))
k=ob.decompressRLElist(nums)
print(' '.join([str(i) for i in k]))