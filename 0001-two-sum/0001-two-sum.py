class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            if nums[i] in h:
                return [h[nums[i]], i]
            diff = target - nums[i]
            h[diff] = i