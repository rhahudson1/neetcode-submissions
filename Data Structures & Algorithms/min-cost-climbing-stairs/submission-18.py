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
            cache[i] = min(dfs(i+1), dfs(i+2)) + cost[i]
            return cache[i]

        return min(dfs(0), dfs(1))
        