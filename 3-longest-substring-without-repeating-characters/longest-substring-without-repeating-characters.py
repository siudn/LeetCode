class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxLength = 0, 0
        h = set()

        for r in range(len(s)):
            while s[r] in h:
                h.remove(s[l])
                l += 1
            h.add(s[r])
            maxLength = max(maxLength, r - l + 1)

        return maxLength