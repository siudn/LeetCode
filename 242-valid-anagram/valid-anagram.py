class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sTimes = {}
        tTimes = {}
        for c in s:
            sTimes[c] = 1 + sTimes.get(c, 0)
        for c in t:
            tTimes[c] = 1 + tTimes.get(c, 0)
        return sTimes == tTimes
        
        
        