class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for i,temp in enumerate(temperatures):
            stack = []
            for j in range(i,len(temperatures)):
                if temperatures[j] < temp:
                    continue
                else:
                    res.append(j-i)
                    break
        return res





        