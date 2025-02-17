from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        res = []

        n = 0
        for num in nums:
            freq[num] += 1
            n = max(n, freq[num])

        buckets = [[] for _ in range (n + 1)]

        for key, value in freq.items():
            buckets[value].append(key)
        
        for i in range(n, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res
