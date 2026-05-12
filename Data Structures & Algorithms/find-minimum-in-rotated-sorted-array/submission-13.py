class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        min = nums[0]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[l]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                return mid
        return False
            