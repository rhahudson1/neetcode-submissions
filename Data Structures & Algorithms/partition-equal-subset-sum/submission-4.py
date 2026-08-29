class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        newDp = [False] * (target + 1)
        for i in range(len(nums)):
            for j in range(1, target+1):
                if j >= nums[i]:
                    newDp[j] = dp[j] or dp[j-i]
                else:
                    newDp[j] = dp[j]
            newDp, dp = dp, newDp
        return dp[target]
        