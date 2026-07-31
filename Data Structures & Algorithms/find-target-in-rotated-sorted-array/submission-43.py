class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l < r:
            m = (r + l) // 2
            # m can become l but never r 
            if nums[m] > nums[r]: 
                # [6,2]
                l = m + 1
            else:
                # [2,6]
                r = m
        pivot = l
        def binarySearch(left,right):
            while left <= right:
                mid = (right + left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        result = binarySearch(0,pivot-1)
        if result != -1:
            return result
        return binarySearch(pivot, len(nums)-1)
