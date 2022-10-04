class Solution(object):
    def findMaxConsecutiveOnes(self,nums):
        result,local_max=0,0
        for n in nums:
            local_max=(local_max+1 if n else 0)
            result=max(result,local_max)
        return result
ob=Solution()
c=int(input())
nums=list(map(int,input().split()))
k=ob.findMaxConsecutiveOnes(nums)
print(k)