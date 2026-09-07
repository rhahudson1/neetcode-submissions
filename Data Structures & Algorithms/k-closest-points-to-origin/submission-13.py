class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = (math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2))
            if len(heap) < k:
                heapq.heappush(heap, (-dist, point[0], point[1]))
            elif heap and heap[0][0] < dist:
                heapq.heapreplace(heap, (-dist, point[0], point[1]))
        res = []
        for i in range(k):
            dist, x,y = heapq.heapppop(heap)
            res.append([x,y])
        return res
        