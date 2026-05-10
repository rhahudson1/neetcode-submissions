class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # given array of intervals, merge all overlapping intervals.
        # output: an array of the non overlapping intervals. 
        # merge all overlapping intervals. 
        '''
        Input: intervals = [[1,3],[1,5],[6,7],[8,10]]

        Output: [[1,5],[6,7],[8,10]

        '''
        # 1) try to create the biggest merged interval. Go until
        # end of the merged interval is < start of the other ones


        # We know that an interval needs to be merged when the start is
        # less than the end of another interval
        # 
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for start,end in intervals:
            lastEnd = res[-1][1]
            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start,end])
        return res




