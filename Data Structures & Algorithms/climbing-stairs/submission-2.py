class Solution:
    def climbStairs(self, n: int) -> int:
        # Input: n (the number of steps to reach the top of staircase)
        # the number of ways from step i is always the same whenever we reahc i
        # Instead of recomputing, we store the result
        cache = [-1] * n
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        print(dfs(0))
        return dfs(0)

        # dfs(0) = dfs(1)[1] + dfs(2)[1] 
        # dfs(1) = dfs(2)[1] + dfs(3)[0]
        