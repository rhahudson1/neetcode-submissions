class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 11 - 3
        # 10 - 2
        # 11 - 3
        # n ^ 0 = n
        res = 0
        # 3 ^ 2 ^ 3 = 0 ^ 2 = 2
        for num in nums:
            res = num ^ res
        return res
