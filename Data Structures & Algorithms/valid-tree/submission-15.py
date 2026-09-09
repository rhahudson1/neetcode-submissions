class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        curPath = set()
        adj = defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        def dfs(node, par):
            if node in curPath:
                return False
            curPath.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei,node):
                    return False
            return True
        return dfs(0,-1) and len(curPath) == n
        
            
        
        