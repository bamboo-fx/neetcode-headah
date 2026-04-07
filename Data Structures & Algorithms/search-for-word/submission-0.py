class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Ok so this is a backtracking problem, meaning its dfs with a decision tree.
        Ok great, so first we have stop condition where we reach i == len(word) basically
        saying that we have found a list of characters that equal to our word thus true.
        Otherwise we do a conditional check for basically when we need to backtrack, and here
        are the 4 conditions: r or c is less than 0, r or c is more than or equal to rows or col
        index, or the value of word is not the same as board[r][c] or r or c is already visited.
        Ok also so we are going to make a tuple for ever value in 2d grid r, c and store in a set
        to keep track of already visited cells.

        Ok after those checks, so true check then false check, then the current r, c might
        work so we add to visited path.

        From there we then we recurse, for the given possible correct cell, we go up, down,
        left, right and increment the index and check if it passes the false conditions and if 
        we can add it to path and continue recursing.

        Then if we reach a dead end this is now where we backtrack, remove from path.

        So this is a nested backtracking function, we recurse through the neighbors until either we
        find true or false, either way we will return the result which tells us true or false
        for given cell. But we also if false or true regardless, at every step back remove from set
        such that we may access that cell in the future


        Alright this is how it works: initialize rows and columns of course, then we iterate
        through rows, iterate through every column call dfs function and see if its true or false.
        Now for the dfs function, its just backtracking, we have our true and false base case conditionals.
        And then we mark the cell as visited, recurse in all 4 directions, if we reach true or if we reach false,
        it will dominoe effect back up, but we store in res, then we remove visited such that we potentially could use
        it in the future, but then we return, return, return, domino affect.
        """

        row, col = len(board), len(board[0])

        def backtracking(r, c, i):
            if i == len(word):
                return True

            # false cases
            if r >= row or c >= col or r < 0 or c < 0 or board[r][c] != word[i]:
                return False

            board[r][c] = '#'
            res = backtracking(r + 1, c, i + 1) or backtracking(r - 1, c, i + 1) or backtracking(r, c + 1, i + 1) or backtracking(r, c - 1, i + 1)
            board[r][c] = word[i]
            return res


        for i in range(row):
            for j in range(col):
                if backtracking(i, j, 0):
                    return True

        return False