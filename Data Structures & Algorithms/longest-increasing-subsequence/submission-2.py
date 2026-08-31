class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i,len(nums)):
                if i + 1 < len(nums) and (nums[i] < nums[j]):
                    cache[i] = max(cache[i], j-i + 1)
        return cache[0]


        