class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        res = []
        subset = []
        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()
                dfs(i+1)
                used[i] = False
        dfs()
        return res