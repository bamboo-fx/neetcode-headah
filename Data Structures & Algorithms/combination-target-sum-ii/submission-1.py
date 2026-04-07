class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtracking(index, comb, curr):
            if comb == target:
                res.append(curr.copy())
                return
            if comb > target or index >= len(candidates):
                return

            curr.append(candidates[index])
            backtracking(index + 1, comb + candidates[index], curr)
            curr.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            backtracking(index + 1, comb, curr)

        backtracking(0, 0, [])
        return res