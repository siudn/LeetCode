class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        seen = {s[0]}
        l, r, length = 0, 1, 1

        while r < len(s):
            if s[r] in seen:
                seen.remove(s[l])
                l += 1
                continue
            seen.add(s[r])
            length = max(length, r - l + 1)
            r += 1

        return length