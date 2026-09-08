class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        taskCounter = Counter(tasks)
        for task in taskCounter.values():
            heapq.heappush(heap, -task)
        q = deque()
        time = 0
        while q or heap:
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([time, cnt])
            if q[0][0] == time:
                time, cnt = q.popleft()
                heapq.heappush(heap, cnt )
            time += 1
        return time

        