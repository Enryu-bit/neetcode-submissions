class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r=0
        l=0
        profit=0
        for i in range(len(prices)):
            if prices[i]>prices[r]:
                r=i
            if prices[i]<prices[l]:
                l=i
                r=l
            profit=max(profit,prices[r]-prices[l])
            print(l,r)
        return profit