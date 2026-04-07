class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        type_dic = {")" : "(", "]" : "[", "}" : "{"}
        for c in s:
            if c in type_dic:
                if stack and stack[-1] == type_dic[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False


        stack = []
        close_par = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in close_par:
                if stack and stack[-1] == close_par[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False