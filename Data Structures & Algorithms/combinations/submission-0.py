class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        def backtracking(index, curr):
            if index > n:
                if len(curr) == k:
                    res.append(curr.copy())
                return
            curr.append(index)
            backtracking(index + 1, curr)
            curr.pop()
            backtracking(index + 1, curr)
        backtracking(1, [])

        return res