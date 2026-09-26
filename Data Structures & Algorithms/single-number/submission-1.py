class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        4 - 100
        1 - 001
        2 - 010
        1 - 001
        2 - 010
        '''
        res = 0 # n ^ 0 = 0
        # entire calcualtion is 0 ^ 4 ^ 1 ^ 2 ^ 1 ^ 2
        # group the duplicates 0 ^ 4 ^ (1 ^ 1) ^ (2 ^ 2)
        # 0 ^ 4 = 4
        # think of XOR as a cancellation operation
        for n in nums:
            res = n ^ res
            # res = 5, 
        return res
