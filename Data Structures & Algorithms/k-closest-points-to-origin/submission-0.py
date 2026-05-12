class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for point in points:
            dist = (Math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2))
            print(dist)