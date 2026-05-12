class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost represents how much it costs to step from i
        cache = [-1] * len(cost)
        def dfs(i):
            if i >= len(cost):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = cache[i] + min(dfs(i+1), dfs(i+2))
            return cache[i]
        return min(dfs(0), dfs(1))