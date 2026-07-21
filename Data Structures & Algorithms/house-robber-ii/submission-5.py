class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        # include the first one or include the last one 
        
        def dfs(i, numLen):
            if i >= numLen:
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] =  max(dfs(i+2) + nums[i], dfs(i+1))
            return cache[i]
        
        return max(dfs(0, len(nums)-1), dfs(1, len(nums)))