class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices ={}
        for i, n in enumerate(nums):
            indices[n] = i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and diff[i] != i:
                return [i, diff[i]]