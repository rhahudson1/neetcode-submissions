class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [float("inf")] * (amount + 1)
        cache[0] = 1
        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    cache[i] = min(cache[i], 1 + cache[i - coin])
            
        if cache[amount] == float("inf"):
            return -1
        return cache[amount]


        