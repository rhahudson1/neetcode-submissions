class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                r = m
            else:
                l = m -1
        pivot = l
        def binarySearch(left,right):
            mid = (left + right) // 2
            while left <= right:
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    return mid
                return -1
        result = binarySearch(0,pivot-1)
        if result != -1:
            return result
        return binarySearch(pivot,len(nums)-1)