class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # nums[i] max jump from that position
        # true if you can reach the last index starting from index 0
        # false if not
        goal = len(nums) - 1
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
            

            
        