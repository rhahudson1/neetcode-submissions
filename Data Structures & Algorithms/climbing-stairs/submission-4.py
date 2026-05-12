class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(k):
            if k > n:
                return 0
            elif k == n:
                return 1
            return dfs(k+1) + dfs(k+2)
        dfs(0)
        # dfs(0) = dfs(1) + dfs(2) 
