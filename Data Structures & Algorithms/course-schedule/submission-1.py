class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisties[i] means you have to take course b before you take course a
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if prevMap[crs] == []:
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            premap[crs] =[]
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True