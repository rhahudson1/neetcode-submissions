class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            rowSet = set()
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowSet:
                    return False
                rowSet.add(board[r][c])
        for c in range(cols):
            colSet = set()
            for r in range(rows):
                if board[r][c] == ".":
                    continue
                if board[r][c] in colSet:
                    return False
                colSet.add(board[r][c])
        return True