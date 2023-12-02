class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(lambda x: x.isalnum(), s)).lower()
        rev = s[::-1]
        if rev == s:
            return True
        return False
