class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        can = candidates.sort()
        def dfs(i, cur, total):
            if total == target:
                res.append(can.copy())
                return
            if target < total or i == len(candidates):
                return
            cur.append(can[i])
            dfs(i+1, cur, total + can[i])

            cur.pop()
            while i + 1 < len(can) and can[i] == can[i+1]:
                i +=1 
            dfs(i+1, cur, total)
        dfs(0,[],0)
        return res