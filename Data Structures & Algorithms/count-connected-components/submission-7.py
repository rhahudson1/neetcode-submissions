class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) > n -1:
            return False
        adjMap = [[] for _ in range(n)]
        for u,v in edges:
            adjMap[u].append(v)
            adjMap[v].append(u)
        res = 0
        visit = [False] * n
        def dfs(node):
            for nei in adjMap[node]:
                if not visit[nei]:
                    visit[nei] = True
        
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                res += 1
                dfs(i)
        return res

        
        