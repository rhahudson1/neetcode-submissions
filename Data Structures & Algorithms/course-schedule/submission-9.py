class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for u,v in prerequisites:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        