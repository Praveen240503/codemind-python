import string
class Solution(object):
    def convertToTitle(self,n):
        alph=string.ascii_uppercase
        res=""
        while n:
            n,r=(n-1)//26,(n-1)%26
            res+=alph[r]
        return (res[::-1])
ob=Solution()
nums=int(input())
k=ob.convertToTitle(nums)
print(k)