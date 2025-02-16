from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        res = []

        n = 0

        for num in nums:
            freq[num] += 1

            if freq[num] > n:
                n = freq[num]

        buckets = [[] for _ in range(n + 1)]
        
        for key, value in freq.items():
            buckets[value].append(key)
        
        while k > 0:
            for i in buckets[n]:
                if k <= 0:
                    break
                res.append(i)
                k -= 1
            n -= 1
                
        return res
