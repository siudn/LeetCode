class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1] * len(nums), [1] * len(nums) 

        curr = 1
        for i in range(len(nums)):
            prefix[i] = curr
            curr *= nums[i]

        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = curr
            curr *= nums[i]
        
        for i in range(len(nums)):
            nums[i] = prefix[i] * postfix[i]
        
        return nums
