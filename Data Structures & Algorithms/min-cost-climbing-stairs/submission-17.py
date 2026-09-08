class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [float("inf")] * len(cost)
        def dfs(i):
            if i >= len(cost):
                return float("inf")
            if i == len(cost):
                return cost[i]
            if cache[i] != float("inf"):
                return cache[i]
            cache[i] = min(dfs(i+1), dfs(i+2))
            return cache[i]
        return dfs(0)
        