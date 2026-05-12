class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l <= r:
            if target == nums[l] + nums[r]:
                return [l, r]
            elif target > nums[l] + nums[r]:
                l += 1
            elif target < nums[l] + nums[r]:
                r -= 1
        return -1