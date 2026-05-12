class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # cache[i] represents the most amount of money you can make at position i
        cache[0] = nums[0]
        cache[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            cache[i] = max(nums[i] + cache[i-2], cache[i-1])
        return cache[len(nums)-1]

        