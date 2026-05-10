class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []  # min-heap holding the k largest so far

        for x in nums:
            self.add(x)  # reuse the same logic

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)  # pop+push in one step
        return self.heap[0]