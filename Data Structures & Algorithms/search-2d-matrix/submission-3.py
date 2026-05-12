class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        lo = 0
        hi = rows - 1
        while lo <= hi:
            mid = (lo + hi) //2
            if target < matrix[mid][0]:
                hi =mid - 1
            elif target > matrix[mid][-1]:
                lo = mid + 1
            else:
                break
        if not (lo <= hi):
            return False
        row = (lo+hi) // 2
        l , r = 0, len(matrix[row])
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid -1
            else:
                l = mid + 1
