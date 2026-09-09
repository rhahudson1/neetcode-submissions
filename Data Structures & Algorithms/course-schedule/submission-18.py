class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        curPath = set()
        def dfs(i):
            if i in curPath:
                return False
            if adj[i] == []:
                return True
            curPath.add(i)
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            curPath.remove(i)
            adj[i] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        