class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        maxProfit = 0
        while r < len(prices):
            print(l,r)
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
                r += 1
            else:
                l += 1
        return maxProfit