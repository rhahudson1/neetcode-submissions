class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        size = 0
        end = 0
        res = []
        for i, n in enumerate(s):
            size += 1
            end = max(end, lastIndex[n])
            if i == end:
                res.append(size)
                size = 0
        return res
                

        