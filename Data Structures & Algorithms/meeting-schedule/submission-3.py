"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # given array intervals. Has elements of (start, end)
        # (0,30) and (5,10) conflict
        # Why? the start time of one, is before the end time of another. 
        # check all of the start times with every single end time. O(n^2) solution.
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        # [(5,8), (9,15),(16,30)]
        # the first end index is 0
        # the first start index is 1
        # run the loop until starte index is greater tahn len - 1
        prev_end = intervals[0].end
        for i in range(1,len(intervals)):
            cur_start = intervals[i].start
            if cur_start < prev_end:
                return False
            prev_end = intervals[i].end
        return True
