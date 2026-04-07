class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        """
        Reconstructing new matrix by building columns based off of rows then comparing
        new matrix with original matrix

        So basically a valid square should contain the same string when looking
        across the row as when looking across the column, so we should first do
        an initial quick sanity check of just see if the row is longest in length
        and if outer column has same length as outer row.

        And then after that we just need to iterate through columns, building
        columns using rows then comparing with original to see if we get the same shape.
        

        cols = 0
        rows = len(words)
        new_words = []
        for word in words:
            cols = max(cols, len(word))

        if cols != len(words[0]) or cols != rows:
            return False

        for col in range(cols):
            new_word = []
            for row in range(rows):
                if col < len(words[row]):
                    new_word.append(words[row][col])

            new_words.append(''.join(new_word))

        return words == new_words
        """

        """
        Alright so a valid square just means kth row is the same as kth column,
        to validate that all we have to do is go through by rows, and in each
        row go through by columns, and ensure the swapped versions are the same,
        but also three checks, that if they are not equal or length of row k and col k
        are different
        """

        for row in range(len(words)):
            for col in range(len(words[row])):
                if col >= len(words) or row >= len(words[col]) or words[row][col] != words[col][row]:
                    return False

        return True