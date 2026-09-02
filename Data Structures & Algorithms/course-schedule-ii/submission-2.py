class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # prereq[i] = [a,b] means you have to take course b first to take a
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        res = []
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                res.append(crs)
                return True
            visitSet.add(crs)
            for c in preMap[crs]:
                if not dfs(c):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
        