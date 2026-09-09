"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            test = res[-1].end
            if test > intervals[i][0]:
                return false
            test = res[-1][1]
        return True
