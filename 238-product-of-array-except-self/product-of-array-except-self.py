class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        res = []
        pre = [1] * length
        post = [1] * length

        for i in range(1, length):
            pre[i] *= nums[i - 1] * pre[i - 1]
        
        for i in range(length - 2, -1, -1):
            post[i] *= nums[i + 1] * post[i + 1]
        
        for i in range(length):
            res.append(pre[i] * post[i])
        
        return res
        
