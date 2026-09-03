class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) > n -1:
            return False
        adjMap = {}
        for u,v in edgeS:
            adjMap[u].append(v)
            adjMap[v].append(u)
        res = 0
        visit = [False] * n
        def dfs(node):
            if visit[node]:
                return False
            visit[node] = True
            for nei in adjMap[node]:
                if not dfs(nei):
                    return False
            res += 1
        for i in range(n):
            if not dfs(i):
                return False
        return res

        
        