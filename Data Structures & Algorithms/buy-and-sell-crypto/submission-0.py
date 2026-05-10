class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_value = 0
        while r < len(prices):
             if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_value = max(max_value, profit)
             else:
                l = r
             r += 1
        return max_value
