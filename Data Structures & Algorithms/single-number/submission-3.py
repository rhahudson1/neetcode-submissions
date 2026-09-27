class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 3 - 011
        # 2 - 010
        # 3 - 011
        res = 0
        # n ^ 0 = n
        # 1) 3 ^ 0 = 3 -> res = 3 
        # 2) 3 ^ 0 = 000 -> res = 11
        # 3) 3 ^ 0 = 010
        for num in nums:
            res = num ^ res
        return res
