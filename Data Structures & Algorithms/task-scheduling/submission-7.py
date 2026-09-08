class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        taskCounter = Counter(tasks)
        for task in taskCounter.values():
            heapq.heappush(heap, - task)
        print(heap)
        