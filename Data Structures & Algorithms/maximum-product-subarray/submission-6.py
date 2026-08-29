class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 0,0 
        for num in nums:
            temp = num * curMax
            curMax = max(temp, num *curMin, num)
            curMin = min(temp, num*curMin, num)
        return curMax

        