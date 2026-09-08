class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        taskCounter = Counter(tasks)
        for task in taskCounter.values():
            heapq.heappush(heap, -task)
        q = deque()
        time = 0
        while q or heap:
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([time + n, cnt])
            if q and q[0][0] == time:
                heapq.heappush(heap, q.popleft()[1] )
            
        return time

        