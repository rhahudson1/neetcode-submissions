class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            product = 1
            for j in range(i+1, len(nums)):
                product *= nums[j]
                cache[i] = max(cache[i], product)
        return max(cache)

        