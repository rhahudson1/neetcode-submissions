class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # connected
        # no cycles
        visitSet = set()
        def dfs(i):
            if i in visitSet:
                return False
            visitSet.add(i)
            if not edges[i]:
                return False
            for nei in edges[i]:
                if not dfs(nei):
                    return False
            visitSet.remove(i)
            return True
        for i in range(n):
            if not dfs(i):
                return False
        return True


        