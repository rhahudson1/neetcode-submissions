class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      l, r = 0, 1
      max_profit = 0
      while r < len(prices):
        if price[r] > price[l]:
            profit = price[r] - price[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        l += 1
      return max_profit