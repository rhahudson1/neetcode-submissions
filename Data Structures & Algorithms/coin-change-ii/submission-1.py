class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Output: the number of distinct combinations that total up to amount
        cache = {}
        def dfs(i, total):
            if total == amount:
                return 1
            if total > amount:
                return 0
            if i == len(coins):
                return 0
            if (i,total) in cache:
                return cache[(i,total)]
            cache[(i,total)] = dfs(i, total + coins[i]) + dfs(i + 1, total)
            return cache[(i,a)]

        return dfs(0,0)


        