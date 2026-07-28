class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l < r:
            mid =(l + r) // 2
            if nums[mid] > nums[r]:
                # if middle is greater than right, the smallest element must be to the right of 
                l = m + 1
            else:
                r = m - 1
        pivot = l
        def binarySearch(left: int, right:int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        result = binarySearch(0,pivot-1)
        if result != -1:
            return result
        return binarySearch(pivot, len(nums))
