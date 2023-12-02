class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            key = tuple(sorted(list(word)))
            print(key)
            if key not in map:
                map[key] = [word]
            else:
                map[key].append(word)

        grouped = list(map.values())
        return grouped

        
