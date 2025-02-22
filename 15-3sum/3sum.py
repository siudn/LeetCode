class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, v in enumerate(nums):
            if v > 0:
                break
            
            if i > 0 and v == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                curr = v + nums[j] + nums[k]
                
                if curr < 0:
                    j += 1
                elif curr > 0:
                    k -= 1
                else:
                    res.append([v, nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res