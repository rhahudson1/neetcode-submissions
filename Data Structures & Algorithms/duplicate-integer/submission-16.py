class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for i in range(len(nums)):
            if nums[i] in numSet:
                return False
            numSet.add(nums[i])
        return True