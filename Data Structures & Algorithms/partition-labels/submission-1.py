class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        res = []
        size = 0
        end = 0
        for i, c in enuemrate(s):
            size += 1
            if i == c[i]:
                res.append(size)
                size = 0
        return res
            
            
            



        