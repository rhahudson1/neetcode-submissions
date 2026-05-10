"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Given array intervals. Objects that have start, end
        # Find the minimum number of rooms required to schedule all meetings
        # They can end and start at same time --> (0,8) and (8,10)
        # Find the number of overlaps
        # [(0,40), (5,10), (15,20)]
        # Room 1 = (0,40)
        # Room 2 = (5,10), (15,20)
        intervals.sort(key=lambda x:x.start)
        min_heap = []
        # store the earliest end time of each room
        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
        return len(min_heap)











        