class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            # you can either rob the house or not rob the house
            print(cache[i])
            return cache[i]
        return dfs(0)