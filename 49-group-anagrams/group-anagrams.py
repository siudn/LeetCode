class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - 97] += 1
                
            d[tuple(count)].append(word)

        return d.values()
            