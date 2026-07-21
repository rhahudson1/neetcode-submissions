class Solution:
    def climbStairs(self, n: int) -> int:
        # given integer representing the number of steps to reach the top of a staircase.
        # Can either climb 1 or 2 steps
        cache = [-1] * n
        def dfs(i):
            if i > n:
                return 0
            elif i == n:
                return 1
            cache[i] = dfs(i) + dfs(i+1)
            return cache[i]
        return cache[0] 

