class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        # can rob the hosue but then have to rob i + 2
        # max between r
        def dfs(i):
            if i > len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return cache[i]
        dfs(0)

        