class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sTimes = {}
        tTimes = {}
        for i in range(len(s)):
            sTimes[s[i]] = 1 + sTimes.get(s[i], 0)
            tTimes[t[i]] = 1 + tTimes.get(t[i], 0)
        return sTimes == tTimes
        
        
        