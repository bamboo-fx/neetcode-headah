class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force
        # check if rows are good
        for row in range(len(board)):
            fixed_row = set()
            for col in range(len(board[0])):
                if board[row][col] in fixed_row:
                    return False
                if board[row][col] == ".":
                    continue
                fixed_row.add(board[row][col])
        # check if columns are good
        for col in range(len(board[0])):
            fixed_col = set()
            for row in range(len(board)):
                if board[row][col] in fixed_col:
                    return False
                if board[row][col] == ".":
                    continue
                fixed_col.add(board[row][col])
        # check if 3x3 boxes are good
        for square in range(9):
            box = set()
            for r in range(3):
                for c in range(3):
                    row = (square // 3) * 3 + r
                    col = (square % 3) * 3 + c
                    if board[row][col] in box:
                        return False
                    if board[row][col] == ".":
                        continue
                    box.add(board[row][col])

        return True

