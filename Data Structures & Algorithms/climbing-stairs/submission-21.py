class Solution:
    def climbStairs(self, n: int) -> int:
        # n represents how many steps between you and the top
        # can either climb 1 or 2
        cache = [-1] * i
        def dp(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if cache != -1:
                return cache[i]
            cache[i] = dp(i+1) + dp(i+2)
        return cache[0]