class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        seen = set()
        def dfs(i):
            if i == len(nums):
                lis = tuple(subset.copy())
                if lis in seen:
                    return
                res.append(subset.copy())
                seen.add(lis)
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

        