class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            dist = (math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2))
            if len(min_heap) < k:
                heapq.heappush(min_heap,(point[0],point[1],dist))
            elif min_heap and min_heap[0][2] < dist:
                heapq.heapreplace(min_heap,(point[0],point[1],dist))
        return (min_heap[0][0],min_heap[0][1])
