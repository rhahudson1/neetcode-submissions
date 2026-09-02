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
        def dfs(i):
            if i in visitSet:
                return False
            visitSet.add(i)
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            visitSet.remove(i)
            return True
        for i in range(n):
            if not dfs(i):
                return False
        return True


        