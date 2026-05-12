class Solution:
    def climbStairs(self, n: int) -> int:
        # n represents how many steps between you and the top
        # can either climb 1 or 2
        def dp(i):
            if i > n:
                return
            if i == n:
                return 1
            return dp(i+1) + dp(i+2)
        return dp(0) + dp(1)