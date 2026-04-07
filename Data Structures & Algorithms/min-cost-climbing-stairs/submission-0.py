class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # index is the position, cost is number in cost array
        # bottom up, start with smallest step

        # optimized
        """
        Hella confusing but basically the logic is: we start from end of array
        so like we can take 1 or 2 steps, cost from last to second to last to
        top of stairs is our base cases, then we want to iteratively increase
        and essentially add to the total cost, we are going down the stairs, but
        actually building total cost array bottom up, space optimized by just choosing
        from two most recent, and then by the time we loop to starting indices 0 or 1,
        we choose which one is better and we have mapped out the entire cost array iteratively
        and then the actual key algorithm here is recognizing:
        cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        right so basically the cost of a given index is going to be the total of
        the cost of taking that step to get to that index itself, as well as the previous
        cost of the steps.
        """

        for i in range(len(cost)-3, -1, -1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])
