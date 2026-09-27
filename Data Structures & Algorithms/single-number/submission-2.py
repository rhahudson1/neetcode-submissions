class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 3 - 011
        # 2 - 010
        # 3 - 011
        res = 0
        # n ^ 0 = n
        # 1) 3 ^ 0 = 3
        # 2) 2 ^ 3 = 001
        # 3) 3 ^ 1 = 010
        for num in nums:
            res = num ^ 0
        return res
