class Solution:

    def encode(self, strs: List[str]) -> str:
        # add a delimiter
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        # res array
        res = []
        # two pointers
        # one is at the number, one increments until delimiter
        # slow becomes delimiter + 1
        # fast becomes number (length)
        # append word in string indexing from slow to fast
        # set slow to current fast, loop again
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = length + i
            res.append(s[i:j])
            i = j
        return res