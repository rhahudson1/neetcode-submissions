class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        hashmap = {}
        def dfs(i):
            if i == len(nums):
                if subset in hashmap:
                    return
                res.append(subset.copy())
                hashmap.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

        