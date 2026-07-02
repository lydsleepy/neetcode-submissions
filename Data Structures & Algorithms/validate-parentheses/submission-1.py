class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }

        stack = []

        for ch in s:
            if ch in valid.keys() and stack and stack[-1] == valid[ch]:
                stack.pop()
            else:
                stack.append(ch)
        
        return len(stack) == 0