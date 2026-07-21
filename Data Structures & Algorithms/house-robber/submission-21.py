class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def dfs(i):
            if cache[i] != -1:
                return cache[i]
            if i > len(nums):
                return 0
            cache[i] = max(nums[i] + dfs(i+2),dfs(i+1))
            return cache[i]
        return max(dfs(0), dfs(1))