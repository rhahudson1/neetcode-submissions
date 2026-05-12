class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # amount represents teh targe tamount
        # coins represents an arrray of differnet denominations
        # return the fewest number of coins to get target
        # return -1 if not possible
        totalCoins = 999999999
        cache = [-1] * (amount + 1)
        cache[0] = 1
        # cahce[i] represents the least number of coins to get to i
        def dfs(i):
            cache[i] = cache[amount-i]
            print(i)
            print(cache[i])
        dfs(0)
        

