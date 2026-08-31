class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [float("inf")] * (amount+1)
        cache[0] = 1
        for i in range(1,amount):
          for coin in coins:
            if amount - coin >= 0:
                cache[i] = min(cache[i], 1 + cache[i-coin])
        res = cache[amount]
        if res == float("inf"):
            return -1
        return res
            


        
        