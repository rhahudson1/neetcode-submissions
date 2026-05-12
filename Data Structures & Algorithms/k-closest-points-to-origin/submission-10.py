class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        # 
        for point in points:
            dist = (math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2))
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist,point[0],point[1]))
            elif max_heap and max_heap[0][0] < dist:
                heapq.heapreplace(max_heap, (dist,point[0],point[1]))
        res = []
        for pt in range(k):
            dist, x1,y1 = heapq.heappop(max_heap)
            res.append([x1,y1])
        return res
