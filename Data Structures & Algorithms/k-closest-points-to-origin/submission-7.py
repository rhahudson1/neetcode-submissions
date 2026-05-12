class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            dist = (math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2))
            if len(min_heap) < len(points) - k + 1:
                heapq.heappush(min_heap,(point[0],point[1],dist))
            elif min_heap and min_heap[0][2] < dist:
                heapq.heapreplace(min_heap,(point[0],point[1],dist))
        res = []
        for pt in min_heap:
            x1, y1, dist = heapq.heappop(min_heap)
            res.append([x1,y1])
        return res
