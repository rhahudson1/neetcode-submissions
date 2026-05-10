class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       dict ={}
       for i, n in enumerate(nums):
            diff = target - n
            if diff in dict:
                return [min(i, dict[diff]), max(i, dict[diff])]
            dict[n] = i
          