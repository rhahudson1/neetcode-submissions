class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l < r:
            m = (r + l) // 2
            if nums[m] < nums[l]: 
                l = m
            else:
                # nums[m] >= nums[l]
                r = m - 1
        pivot = l
        print(l)
        return l
