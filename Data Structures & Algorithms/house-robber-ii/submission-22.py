class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def dfs(i,allowed):
            if i >= len(allowed):
                return 0
            if cache != -1:
                return cache[i]
            cache[i] = max(allowed[i] + dfs(i+2, allowed), dfs(i+1,allowed))
            return cache[i]
        res = max(dfs(0,nums[0:len(nums)-1]), dfs(0, nums[1:len(nums)]))
        return res
            
        