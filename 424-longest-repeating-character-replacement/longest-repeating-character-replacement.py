from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)

        counts = defaultdict(int)
        l, r, res, maxChar = 0, 0, 1, 0

        while r < len(s):
            counts[s[r]] += 1

            for i in counts:
                maxChar = max(maxChar, counts[i])

            if r - l + 1 - maxChar > k:
                counts[s[l]] -= 1
                l += 1
            else:
                res = max(res, r - l + 1)
            r += 1
        
        return res