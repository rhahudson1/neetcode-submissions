class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        print(maxHeap)
        heapq.heapify(maxHeap)
        print(maxHeap)