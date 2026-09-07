class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stoneS:
            if len(heap) < 2:
                heapq.heappush(heap, stone)
            heapq.heapreplace(heap, heap[1] - heap[0])
            heapq.heappush(stone)
        print(heap)
        
        