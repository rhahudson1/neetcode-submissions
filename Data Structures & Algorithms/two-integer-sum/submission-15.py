class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices ={}
        for i, n in enumerate(nums):
            indicies[n] = i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]