class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            dist = (math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2))
            heapq.heappush(min_heap, (dist,point[0],point[1]))
        res = []
        for pt in range(k):
            dist, x1,y1 = heapq.heappop(min_heap)
            res.append([x1,y1])
        return res
