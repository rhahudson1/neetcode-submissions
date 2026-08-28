class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def dfs(i,allowed):
            if i >= len(allowed):
                return 0
            if cache != -1:
                return cache[i]
            cache[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return cache[i]
        res = max(dfs(0,nums[0:len(nums)-1]), dfs(0, nums[1:len(nums)]))
        return res
            
        