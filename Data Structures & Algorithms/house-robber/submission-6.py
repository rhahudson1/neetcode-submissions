class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums[i] represents the maount of money the ith house has
        # cannot rob ajacent houses
        # return max amount of money you can rob without alerting the police
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        # you either rob the house, or you go to the next one
