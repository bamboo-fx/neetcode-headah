class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort all strings, when sorted they are same
        # use sorted strings as keys, add values as the string unsorted
        # return just the values
        tracker = {}
        for string in strs:
            key = "".join(sorted(string))
            if key not in tracker:
                tracker[key] = []

            tracker[key].append(string)

        return list(tracker.values())