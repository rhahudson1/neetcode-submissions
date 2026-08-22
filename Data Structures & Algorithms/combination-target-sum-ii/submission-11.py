class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []
        def dfs(i, cur):
            if cur == target: 
                res.append(subset.copy())
                return
            if i == len(candidates) or cur > target:
                return
            subset.append(candidates[i])
            dfs(i+1, cur + candidates[i])
            subset.pop()
            dfs(i+1, cur + candidates[i])
        dfs(0,0)
        return res
            

        