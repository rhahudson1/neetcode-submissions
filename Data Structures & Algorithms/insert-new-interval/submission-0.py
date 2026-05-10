class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals sorted by start
        # need to insert the interval into a new list. 
        # iterate over intervals and keep appending to new intervals
        # until either start of new interval is 
        res = []
        '''
        1) check if the interval in intervals is overlapping with newInterval.
        2) if no, then it will append to res
        3) if yes, add it to cur_interval.
        - minimum of start, and max of end
        - Check to see if cur interval overlaps with other intervals
        4) once it doesn't just append to res
        '''
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res

