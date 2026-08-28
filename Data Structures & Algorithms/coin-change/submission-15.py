class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(i):
            if ammount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            res = float("inf")
            for coin in coins:
                if amount - coun >= 0:
                    res = min(res, 1 + dfs(amount-coin))
            memo[amount] = res
            return res
        minCoins = dfs(amount)
        if minCoints == float("inf"):
            return -1
        return minCoins


