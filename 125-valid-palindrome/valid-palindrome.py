class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(lambda x: x.isalnum(), s)).lower()
        
        if len(s) == 0 or len(s) == 1:
            return True
    
        left = 0
        right = len(s) - 1

        while (left < right):
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        