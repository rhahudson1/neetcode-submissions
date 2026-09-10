class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # nums[i] max jump from that position
        # true if you can reach the last index starting from index 0
        # false if not
        curIdx = 0
        for i, num in enumerate(nums):
            if curIdx == len(nums)-1:
                return True
            if i == curIdx:
                curIdx += nums[curIdx]
        return False
        
        