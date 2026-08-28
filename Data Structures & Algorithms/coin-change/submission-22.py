class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [float("inf")] * (amount+1)
        cache[0] = 0
        for a in range(1,amount+1):
            for coin in coins:
                if a - coin >= 0:
                    cache[a] = min(cache[0], cache[a-coin] + 1)
        if cache[-1] == float("inf"):
            return -1
        return cache[-1]