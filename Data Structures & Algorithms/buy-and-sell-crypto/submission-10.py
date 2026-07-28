class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxProfit = 0
        while r <= len(prices)-1:
            profit = prices[r] - prices[l]
            if profit > maxProfit:
                maxProfit = profit
            if r > l:
                r += 1
            else:
                l += 1
        return profit
        