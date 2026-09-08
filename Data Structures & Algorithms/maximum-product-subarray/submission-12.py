class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1,1
        for num in nums:
            temp = curMin * num
            curMin = min(curMin, curMax * num, curMin * num)
            curMax = max(curMax, curMax * num, temp * num)
            res = max(res, curMax)
        return res



        