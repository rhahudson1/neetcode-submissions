class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones list represents weight of each stone
        # choose 2 heaviest stones and msash them.
        # if the same, both stones are destroyed
        # if one is greater than the other, 
        heap = []
        for i in range(len(stones)):
            heapq.heappush(heap,-stones[i])
        while len(strones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        heap.append(0)
        return abs(stones[0])
