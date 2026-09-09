class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        adj = defaultdict(list)
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        visitSet = [False] * n
        def dfs(i):
            for nei in adj[i]:
                if not dfs(nei):
                    visitSet[i] = True
                    dfs(nei)
        
        for i in range(n):
            if not visitSet[i]:
                visit[i] = True
                dfs(i)
                res += 1
        return res

        