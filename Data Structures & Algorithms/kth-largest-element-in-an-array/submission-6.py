class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
            elif minHeap and minHeap[0] < num:
                heapq.heapreplace(minHeap, num)
        return minHeap[0]