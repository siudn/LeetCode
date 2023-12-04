from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        opening = ["(","{","["]
        top = -1

        for c in s:
            if c in opening:
                stack.append(c)
                top += 1
                continue
            if top > -1:
                if c == "]":
                    if stack[top] != "[":
                        return False
                    stack.pop()
                    top -= 1
                elif c == "}":
                    if stack[top] != "{":
                        return False
                    stack.pop()
                    top -= 1
                elif c == ")":
                    if stack[top] != "(":
                        return False
                    stack.pop()
                    top -= 1
            else:
                return False
        
        return not stack
            
        