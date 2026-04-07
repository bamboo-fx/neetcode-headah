class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        move from right to left, first its -1 always, keep track of a max, compare
        with the max.

        Wait so i should start at the second to last one, compare it with the
        previous arr value, if less change and 
        """
        max_score = arr[-1]
        # linear time and constant space
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = max_score
            max_score = max(max_score, temp)
        arr[-1] = -1
        return arr

