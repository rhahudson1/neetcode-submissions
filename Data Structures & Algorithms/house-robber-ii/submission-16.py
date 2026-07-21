class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def robline(arr):
            if len(arr) == 1:
                return arr[0]
            cache = [-1] * len(arr)
            cache[0] = arr[0]
            cache[1] = max(arr[0], arr[1])
            for i in range(2,len(arr)):
                cache[i] = max(nums[i] + cache[i-2], cache[i-1])
            return cache[len(arr)-1]
        return max(robline(arr[:-1]), robline(arr[1:]))
        