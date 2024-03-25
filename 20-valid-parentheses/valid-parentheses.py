from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        d = {')':'(','}':'{',']':'['}

        for char in s:
            
            if char in d:
                if not stack or stack[-1] != d[char]:
                    return False
                stack.pop()
                continue

            stack.append(char)

        return not stack
        