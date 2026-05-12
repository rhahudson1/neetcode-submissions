class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        result = 1
        for i in range(len(nums)):
            res[i] = result
            result *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] = postfix * res[i]
            result = nums[i] * res[i]
        
        return res
        
        