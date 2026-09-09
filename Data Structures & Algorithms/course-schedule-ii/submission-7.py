class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(list)
        for crs, pr in prerequisites:
            pre[crs].append(pr)
        res = []
        curPath = set()
        doneSet = set()
        def dfs(i):
            if i in curPath:
                return False
            if i in doneSet:
                return True
            curPath.add(i)
            for nei in pre[i]:
                if not dfs(i):
                    return False
            curPath.remove(i)
            doneSet.add(i)
            res.append(i)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        