class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        lo = 0
        hi = cols - 1
        while lo <= hi:
            mid_row = (lo + hi) // 2
            if matrix[mid_row][0] > target:
                lo = mid_row - 1
            elif matrix[mid_row][-1] < target:
                hi = mid_row + 1
            else:
                break
        if not (hi <= lo):
            return False
        mid_row = (lo + hi) // 2
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
