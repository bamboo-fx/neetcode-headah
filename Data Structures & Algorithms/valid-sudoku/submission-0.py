class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force
        for i in range(len(board)):
            stored = set()
            for j in range(len(board[0])):
                if board[i][j] in stored:
                    return False
                if board[i][j] != ".":
                    stored.add(board[i][j])

        for k in range(len(board[0])):
            rows = set()
            for l in range(len(board)):
                if board[l][k] in rows:
                    return False
                if board[l][k] != ".":
                    rows.add(board[l][k])

        for square in range(9):
            box = set()
            for r in range(3):
                for c in range(3):
                    row = (square // 3) * 3 + r
                    col = (square % 3) * 3 + c
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in box:
                        return False

                    box.add(board[row][col])
        return True