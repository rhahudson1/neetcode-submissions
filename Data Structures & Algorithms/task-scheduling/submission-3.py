class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        '''
        A:3
        B:3
        '''
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        '''
        if counts were [3,3], heap becomes [-3,-3]
        '''
        time = 0
        q = deque()
        while maxHeap or q:
            # keep it running until no tasks are left in the heap and no tasks are cooling
            time += 1
            if not maxHeap:
                time = q[0][1]
            # If maxHeap is empty, that means all tasks are cooling. So, instead of increasing time by one, jump directly to when the next task becomes available.
            cnt = 1 + heapq.heappop(maxHeap)
            #means we executed teh task once

            if cnt:
                q.append([cnt, time + n])
                # basically saying hey, this is when I am avialabel next
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
