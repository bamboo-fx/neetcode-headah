class Solution:
    def isValid(self, s: str) -> bool:
        """
        The logic is that we do a stack ds/a where we have a hashmap of
        corresponding bracket, and its stack so we do LIFO, so basically most
        recent is last in, right and so we iterate through s, when we reach
        a closing bracket, because of LIFO.

        Ok so since its a stack, we are iterating through and popping from
        the end right, so basically if stack is empty return true else return
        false. Now the way to pop is when we iterate.

        Yes so the logic is we make a separate stack that we are adding to,
        we only add to it if its an open bracket, if its a closing bracket,
        then due to nature of stack and LIFO, we check if its recent stack
        is opening if its the corresponding opening to our closing, if not
        return false, else then we remove that corresponding opening and continue.
        At the end if we have a stack return false if nothing return true
        """

        bracket = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for c in s:
            if c in bracket:
                if stack and stack[-1] == bracket[c]:
                    stack.pop()

            else:
                stack.append(c)

        return True if not stack else False
        