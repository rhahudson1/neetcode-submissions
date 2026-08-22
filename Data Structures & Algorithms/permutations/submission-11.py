class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        used = [False] * len(nums)
        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    subset.append(nums[i])
                    used[i] = True
                    dfs()
                    subset.pop()
                    dfs()
                    user[i] = False
        dfs()
        return res
                
