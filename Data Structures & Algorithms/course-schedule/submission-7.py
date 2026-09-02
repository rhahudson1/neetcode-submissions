class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for pre, crs in prerequisites:
            preMap[crs].append(pre)
        print(preMap)
        