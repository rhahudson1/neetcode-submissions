class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # 1) If the end of the new interval is before the start
            if newInterval[1] < interval[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # 2) IF the start of the new interval is after the end of the interval
            elif newInterval[0] > interval[i][1]:
                res.append(newInterval)
            else:
                newInterval = [
                    min(newInterval[0], interval[i][0]),
                    max(newInterval[1], interval[i][1])
                ]
        return res


        