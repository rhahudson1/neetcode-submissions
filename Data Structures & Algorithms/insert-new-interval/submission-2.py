class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i,interval in enumerate(intervals):
            # 1) the newInterval is infront of the whole intervals. 
            # - we append newInterval and then everythign else in intervals
            # 2) the newinterval is behind the whole intervals[i], in which case 
            # - append interval
            # 3) there is an overlap.
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1],interval[1])
                ]
        res.append(newInterval)
        return res