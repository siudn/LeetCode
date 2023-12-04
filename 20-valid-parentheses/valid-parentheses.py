from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        h = {")" : "(" , "]" : "[" , "}" : "{"}

        for c in s:
            if c not in h:
                stack.append(c)
                continue
            if not stack or stack[-1] != h[c]:
                return False
            stack.pop()

        return not stack
            
        