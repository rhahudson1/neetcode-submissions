class Solution:
    def rob(self, nums: List[int]) -> int:
    # thing about a circle
    # you can rob the first house but not include the last house
    # can not rob the first house but can include the last hosue
    # try algo from nums[1:] or nums[:-1]
        if len(nums) == 1:
            return nums[0]
        def maxValue(nums):
            cache = [-1] * len(nums)
            def dfs(i):
                if i >= len(nums):
                    return 0
                if cache[i] != -1:
                    return cache[i]
                cache[i] = max(nums[i] + dfs(i+2), dfs(i+1))
                return cache[i]
            return dfs(0)
        return max(maxValue(nums[1:]), maxValue(nums[:-1]))
        