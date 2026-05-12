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
        start = []
        end = []
        for s, e in intervals:
            start.append(s)
            end.append(e)
        for s in start:
            for e in end:
                if s < e:
                    return False
        return True
