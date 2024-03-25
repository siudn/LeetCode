from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif char == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        
        return not stack
        