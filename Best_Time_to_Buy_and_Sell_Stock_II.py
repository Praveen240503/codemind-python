class Solution:
    def maxProfit(self,prices):
        prev=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prev<prices[i]:
                profit+=prices[i]-prev
            prev=prices[i]
        return profit
ob=Solution()
c=int(input())
prices=list(map(int,input().split()))
k=ob.maxProfit(prices)
print(k)