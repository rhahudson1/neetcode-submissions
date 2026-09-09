class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[u].append(v)
            adj[v].append(u)
        curPath = set()
        def dfs(i):
            if i in curPath:
                return False
            if adj[i] == []:
                return True
            for pre in adj[i]:
                if not dfs(pre):
                    return False
            curPath.remove(i)
            adj[i] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


        