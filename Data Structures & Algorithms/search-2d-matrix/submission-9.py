class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bot = rows - 1
        while top <= bot:
            mid_row = (top + bot) // 2
            if matrix[mid_row][0] > target:
                bot = mid_row - 1
            elif matrix[mid_row][-1] < target:
                top = mid_row + 1
            else:
                break
        if not (top <= bot):
            return False
        mid_row = (top + bot) // 2
        l = 0
        r = len(matrix[mid_row]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid_row][mid] > target:
                r = mid - 1
            elif matrix[mid_row][mid] < target:
                l = mid + 1
            elif matrix[mid_row][mid] == target:
                return True
        return False
