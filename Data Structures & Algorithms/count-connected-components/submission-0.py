class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Input: You are given an integer n (number of nodes) and an array edges (edges[i] = [a, b])
        # Iterate through each edge and connect them to each other. 
        # Add them to a visit set. 
        # Output: Return the number of islands
        adj = {i: [] for i in range(n)}
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        visit = set()
        numIslands = 0
        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for edg in adj[i]:
                if edg not in visit:
                    dfs(edg)
            
            
        for i in range(n):
            if i not in visit:
                dfs(i)
                numIslands+= 1
        return numIslands
