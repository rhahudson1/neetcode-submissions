class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if second > first:
                heapq.heappush(heap, first - second)
        stones.append(0)
        return abs(heap[0])
            



        
        