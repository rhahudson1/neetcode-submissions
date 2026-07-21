class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robline(arr):
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]
            cache = [-1] * len(nums)
            cache[0] = arr[0]
            cache[1] = max(arr[1], arr[0])
            for i in range(2,len(arr)):
                cache[i] = max(nums[i] + robline(arr[i+2:]), robline(arr[i+1:]))
        return max(robline(nums[:-1]), robline(nums[1:]))