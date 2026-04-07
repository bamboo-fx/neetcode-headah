class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n < 2:
            return 1

        step0 = 0
        step1 = 1
        step2 = 1
        for _ in range(3, n + 1):
            temp2 = step2
            temp1 = step1
            total = step0 + step1 + step2
            step2 = total
            step1 = temp2
            step0 = temp1
        
        return step2