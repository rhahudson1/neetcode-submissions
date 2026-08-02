class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0
        for r in range(1,len(prices)):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxProfit = max(maxProfit, profit)
            if prices[l] > prices[r]:
                l = r 
            r += 1
        return maxProfit
