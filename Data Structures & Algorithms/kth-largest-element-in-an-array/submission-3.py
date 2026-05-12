class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap 
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            if heap[0] > num:
                heapq.heapreplace(heap, num)
        return heap[0]