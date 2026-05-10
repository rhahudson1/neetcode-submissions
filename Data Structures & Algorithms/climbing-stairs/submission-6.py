class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(k):
            if k > n:
                return 0
            if k == n:
                return 1
            if cache[k] != -1:
                return cache[k]
            cache[k] = dfs(k+1) + dfs(k+2)
            return cache[k]
        return dfs(0)
        # dfs(0) = dfs(1) + dfs(2) 
