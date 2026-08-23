from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        seen = set()

        def dfs(i):
            if i == len(nums):
                key = tuple(subset)
                if key in seen:
                    return
                seen.add(key)
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res