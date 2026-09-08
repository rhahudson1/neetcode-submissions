class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        if target % 2:
            return False
        
        dp = set()
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
            dp = nextDP
        if target in dp:
            return True
        return False



        