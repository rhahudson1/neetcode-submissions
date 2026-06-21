class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict:
                return [min(i, dict[target - num]), max(i, dict[target - num])]
            dict[num] = i