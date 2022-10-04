def findMaxProfit(prices,i,k,buy,v):
    if (i>=len(prices) or k<=0):
        return 0
    if (v[i][buy]!=-1):
        return v[i][buy]
    if (buy):
        v[i][buy]=max(-prices[i]+findMaxProfit(prices,i+1,k,not buy,v),findMaxProfit(prices,i+1,k,buy,v))
        return v[i][buy]
    else:
        v[i][buy]=max(prices[i]+findMaxProfit(prices,i+1,k-1,not buy,v),findMaxProfit(prices,i+1,k,buy,v))
        return v[i][buy]
def maxProfit(prices):
    n=len(prices)
    v=[[-1 for x in range(2)]for y in range(n)]
    return findMaxProfit(prices,0,1,1,v)
if __name__=="__main__":
    n=int(input())
    prices=list(map(int,input().split()))
    ans=maxProfit(prices)
    print(ans)