class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSums = { 0: 1}
        curSum = 0
        for r in range(len(nums)):
            curSum += nums[r]
            diff = curSum - k
            if diff in prefixSums:
                res += prefixSums[diff]
            prefixSums[curSum] = 1 + prefixSums.get(diff,0)
        return res