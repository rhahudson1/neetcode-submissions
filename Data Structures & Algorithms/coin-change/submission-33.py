class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [-1] * (amount + 1)
        def dfs(i):
            if i > amount + 1:
                return float("inf")
            if cache[i] != -1:
                return cache[i]
            for coin in coins:
                cache[i] = min(cache[i], 1 + dfs(amount - i))
            return cache[i]
        return dfs(0)


        