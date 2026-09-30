class Solution:
    def hammingWeight(self, n: int) -> int:
        # 23 -           16 8 4 2 1
        # 23 -           1 0 1 1 1
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res





        