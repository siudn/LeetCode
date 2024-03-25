from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')':
                if len(stack) >= 1 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif char == '}':
                if len(stack) >= 1 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                if len(stack) >= 1 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        
        return False
        