class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # [6, 7, 0, 1, 2, 4, 5]
        
        # [3, 1, 2]

        while l <= r:
            if nums[r] >= nums[l]:
                return nums[l]

            mid = (l + r) // 2

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid


            

