from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        res = []

        for s in strs:
            groups["".join(sorted(s))].append(s)
        
        for group in groups.values():
            res.append(group)
        
        return res

