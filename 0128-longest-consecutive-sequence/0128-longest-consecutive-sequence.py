class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
    
        h = set(nums)
        l = 0

        for num in h:
            if num - 1 not in h:
                newLen = 1
                curr = num
                while curr + 1 in h:
                    newLen += 1
                    curr += 1
                l = max(l, newLen)

        return l
