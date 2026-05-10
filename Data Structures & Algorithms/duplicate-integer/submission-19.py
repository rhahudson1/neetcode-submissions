class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        charSet = set()
        for num in nums:
            if num not in charSet:
                charSet.add(num)
            else:
                return True
        return False