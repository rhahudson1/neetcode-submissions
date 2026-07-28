class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[l]:
                r = mid - 1
            else:
                l = mid
        pivot = mid
        def binarySearch(left: int, right:int) -> int:
            mid = (right + left) // 2
            while left <= right:
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
        return binarySearch(pivot,len(nums)-1)
            


        