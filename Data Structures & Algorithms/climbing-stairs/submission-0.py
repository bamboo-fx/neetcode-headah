class Solution:
    def climbStairs(self, n: int) -> int:
        # data structure, nothing, just two integer variables
        # algorithm? bottom up dp
        # base case
        if n <= 1:
            return 1
        
        top = 1
        minus_top = 1

        for _ in range(2, n + 1):
            temp = minus_top
            total = top + minus_top
            minus_top = total
            top = temp
        
        return minus_top