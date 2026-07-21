class Solution:
    def rob(self, nums: List[int]) -> int:
        # can either rob the house you are at or go to i + 2 house
        cache = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            cache[i] = max(dfs(i+2) + nums[i],dfs(i+1))
            return cache[i]
        return max(dfs(0), dfs(1))
            


        