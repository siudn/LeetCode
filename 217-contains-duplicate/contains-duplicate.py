class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        traversal = len(nums) - 1
        for i in range(traversal):
            if (nums[i] == nums[i + 1]):
                return True
        return False
        
        