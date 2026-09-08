class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [float("inf")] * (amount + 1)
        cache[0] = 1
        def dfs(i):
            if i > amount + 1:
                return float("inf")
            if cache[i] != -1:
                return cache[i]
            for coin in coins:
                cache[i] = min(cache[i], 1 + dfs(amount - coin))
            return cache[i]
        if cache[amount] == float("inf"):
            return -1
        return cache[amount]


        