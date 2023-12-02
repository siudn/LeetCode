class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            key = tuple(sorted(list(word)))
            if key not in map:
                map[key] = [word]
            else:
                map[key].append(word)

        return list(map.values())
  

        
