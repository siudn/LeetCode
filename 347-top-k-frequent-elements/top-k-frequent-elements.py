class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        topFreq = sorted(d.values(), reverse=True)[:k]
        keys = []

        for key in d:
            if d[key] in topFreq:
                keys.append(key)

        return keys 
