class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        contiguous array of size 3, sum everything, find average, increment if greater than threshold
        """

        l = 0
        sum_tracker = 0
        output = 0
        for r in range(len(arr)):
            sum_tracker += arr[r]

            if r - l + 1 == k:
                avg = sum_tracker / k

                if avg >= threshold:
                    output += 1
                sum_tracker -= arr[l]
                l += 1
            avg = 0

        return output