class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bot = rows - 1
        while top <= bot:
            mid = (top + bot) //2
            if matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
        if not (top <= bot):
            return False
        mid = (top + bot) // 2
        l, r = 0, len(matrix[mid])
        while l <= r:
            m = (l + r) //2
            if matrix[mid][m] == target:
                return m
            elif matrix[mid][m] > target:
                r = m - 1
            else:
                l = m +1
        return False

