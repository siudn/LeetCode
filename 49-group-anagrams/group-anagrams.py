class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        result = []

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - 97] += 1
            if tuple(count) in d:
                d[tuple(count)].append(word)
            else:
                d[tuple(count)] = [word]

        return list(d.values())
            