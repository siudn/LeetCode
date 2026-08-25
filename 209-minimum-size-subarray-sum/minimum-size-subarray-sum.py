class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        length = len(nums) + 1

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                length = min(length, r - l + 1)
                total -= nums[l]
                l += 1
        
        return 0 if length > len(nums) else length