class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # amount represents teh targe tamount
        # coins represents an arrray of differnet denominations
        # return the fewest number of coins to get target
        # return -1 if not possible
        memo = {}

        # cahce[i] represents the least number of coins to get to i
        def dfs(i):
            # i represents the remaining amount
            if i == 0:
                return 0
            if memo[i] != -1:
                return memo[i]
            minCoins = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            memo[amount] = res
            return res
        minCoins = dfs(amount)
        if minCoins == float("inf"):
            return - 1
        return minCoins
        

