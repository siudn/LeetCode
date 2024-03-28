class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        res = []
        pre = [1] * length
        post = [1] * length

        pre[0] = nums[0]
        post[length - 1] = nums[length - 1]

        for i in range(1, length):
            pre[i] *= pre[i - 1] * nums[i]

        for i in range(length - 2, -1, -1):
            post[i] *= post[i + 1] * nums[i]

        for i in range(length):
            if i == 0:
                res.append(post[i + 1])
                continue
            elif i == length - 1:
                res.append(pre[i - 1])
                continue
            res.append(pre[i - 1] * post[i + 1])
        
        return res
            