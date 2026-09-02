class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # connected
        # no cycles
        if len(edges) > (n - 1):
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visitSet = set()
        def dfs(i, par):
            if i in visitSet:
                return False
            visitSet.add(i)
            for nei in adj[i]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            visitSet.remove(i)
            return True
        return dfs(0,-1) and len(visit) == n


        