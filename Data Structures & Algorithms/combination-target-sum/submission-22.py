class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, cur):
            if cur == target:
                res.append(subset.copy())
                return
            if cur > total or i > len(nums):
                return
            subset.append(nums[i])
            dfs(i+1, cur + nums[i])
            subset.pop()
            dfs(i+1, cur)
        dfs(0,0)
        return res

        