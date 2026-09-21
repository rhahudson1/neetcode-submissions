class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # you can either subtract or add the number to the total
        # return the number of different ways that you can build the epxression to ttoal 
        cache = {}
        def dfs(i,total):
            if i > len(nums):
                return 0
            if i == len(nums) and total == target:
                return 1
            cache[(i,total)] = dfs(i+1,total - nums[i]) + dfs(i+1, total + nums[i])
            return cache[(i,total)]
        return dfs(0,0)
        