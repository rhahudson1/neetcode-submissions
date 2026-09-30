class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 11 - 3
        # 10 - 2
        # 11 - 3
        # n ^ 0 = n
        res = 0

        for num in nums:
            res = num ^ 0
        return res
