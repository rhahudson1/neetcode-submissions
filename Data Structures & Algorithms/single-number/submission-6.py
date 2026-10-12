class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # n ^ 0 = n
        # 3 ^ 2 ^ 3 => 3 ^ 3 ^ 2 = 
        res = 0
        for num in nums:
            res = num ^ 0 
        return res
