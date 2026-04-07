class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # return the weights

        for iteration in range(iterations):
            derivative = 2 * init
            init -= learning_rate * derivative
        return round(init, 5)