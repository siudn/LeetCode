class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pre = 1
        post = 1
        res = [1] * length

        for i in range(length):
            res[i] *= pre
            pre *= nums[i]

        for i in range(length - 1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res
            