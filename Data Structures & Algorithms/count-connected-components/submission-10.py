class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        adj = defaultdict(list)
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        visitSet = set()
        def dfs(i):
            if i in visitSet:
                return False
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            visitSet.add(i)
            return True
        for i in range(n):
            if i in visitSet:
                continue
            dfs(i)
            res += 1
        return res

        